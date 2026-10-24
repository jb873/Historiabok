import json, sys
from shapely.geometry import shape, Polygon, box, mapping
from shapely.ops import unary_union, transform
from pyproj import Transformer
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.patheffects as pe

S = sys.argv[1]
HB = S + "/hb/historical-basemaps/geojson/world_1815.geojson"
NE = S + "/ne/geojson/"
import glob
for f in glob.glob(S + "/gf/ofl/crimsontext/*.ttf"): fm.fontManager.addfont(f)
FONT = "Crimson Text"

def load(p): return json.load(open(p, encoding="utf-8"))["features"]

hb = [(f["properties"].get("NAME"), f["properties"].get("SUBJECTO"), shape(f["geometry"]).buffer(0)) for f in load(HB)]
ne = {f["properties"]["ADMIN"]: shape(f["geometry"]).buffer(0) for f in load(NE + "ne_50m_admin_0_countries.geojson")}
land = unary_union([shape(f["geometry"]).buffer(0) for f in load(NE + "ne_50m_land.geojson")])

VIEW = box(-8, 39.5, 20, 57)
land = land.intersection(VIEW)

def hbu(*names):
    return unary_union([g for n, s, g in hb if n in names]).intersection(VIEW)

nice = Polygon([(7.19,43.65),(7.05,43.95),(6.86,44.33),(6.95,44.46),(7.35,44.22),(7.7,44.12),(7.53,43.77)])
sard = unary_union([hbu("Kingdom of Sardinia"), nice])
fr = ne["France"].intersection(box(-6, 41, 10, 52)).difference(sard)
nl = unary_union([ne["Netherlands"], ne["Belgium"]])
lux = ne["Luxembourg"]
ch = ne["Switzerland"]
fixed = unary_union([fr, nl, lux, ch])

prussia_all = hbu("Prussia")
prw = unary_union([g for g in getattr(prussia_all, "geoms", [prussia_all]) if g.centroid.x < 10]).difference(fixed)
pre = unary_union([g for g in getattr(prussia_all, "geoms", [prussia_all]) if g.centroid.x >= 10]).difference(fixed)
sard = sard.difference(unary_union([fr, ch]))

german = ["Palatinate","Hohenzollern","Baden","Saxony","Mecklenburg-Strelitz","Grand Duchy of Hesse","Nassau","Wetzlar",
 "Waldeck","Lippe-Detmold","Brunswick","Anhalt","Mecklenburg-Schwerin","Thuringia","Lübeck","Oldenburg","Hanover",
 "Electoral Hesse","Bremen","Cuxhaven","Holstein","Hamburg","Schaumburg-Lippe","Bavaria","Württemberg"]
italian = ["Lombardy","Venetia","Parma","Papal States","Pontremoli","Fivizzano","Lucca","Tuscany","Modena","Massa","Kingdom of the Two Sicilies","San Marino"]

layers = []
P = "#e9dcbd"  # pergament-land
def add(geom, fc, ec="#8a7a5c", lw=0.5): layers.append((geom.intersection(land), fc, ec, lw))

# övrigt land först
add(land, P, "none", 0)
skip = set(german + italian + ["Prussia","Kingdom of Sardinia","France","Switzerland","Luxembourg"])
for n, s, g in hb:
    if n in skip or n is None: continue
    if "Netherlands" in str(s): continue
    add(g.intersection(VIEW).difference(fixed).difference(sard), P)
pal_de = ["#e8d6ae","#ecdcb8","#e3cfa3","#efe0bf"]
for i, n in enumerate(german):
    add(hbu(n).difference(fixed), pal_de[i % 4], "#8a7a5c", 0.45)
pal_it = ["#e7d2b8","#dccfa9","#e9c9b0","#d8d4b2","#e3d9b6"]
for i, n in enumerate(italian):
    add(hbu(n).difference(fixed), pal_it[i % 5], "#8a7a5c", 0.45)
GR = "#4f7a52"
add(pre, "#a9c2a4", "#5d6f58", 0.6)
add(fr, "#a29d97", "#5f5a55", 0.8)
add(lux, "#e8d6ae", "#8a7a5c", 0.45)
for g in (nl, ch, prw, sard): add(g, GR, "#2f4a31", 0.8)

body = layers[1:]
cover = unary_union([g for g, *_ in body if not g.is_empty])
gaps = land.difference(cover)
gaps = [g for g in getattr(gaps, "geoms", [gaps]) if g.area > 0]
idx = list(range(len(body)))
for gp in gaps:
    if gp.area > 0.5: continue
    best = min(idx, key=lambda i: body[i][0].distance(gp) if not body[i][0].is_empty else 1e9)
    g, fc, ec, lw = body[best]
    body[best] = (unary_union([g, gp]).intersection(land), fc, ec, lw)
layers = [layers[0]] + body

tr = Transformer.from_crs("EPSG:4326", "+proj=laea +lat_0=48 +lon_0=7 +units=m", always_xy=True)
proj = lambda g: transform(tr.transform, g)

def patch(geom, **kw):
    polys = [geom] if geom.geom_type == "Polygon" else [p for p in getattr(geom, "geoms", []) if p.geom_type == "Polygon"]
    verts, codes = [], []
    for p in polys:
        for ring in [p.exterior] + list(p.interiors):
            c = list(ring.coords); verts += c; codes += [Path.MOVETO] + [Path.LINETO]*(len(c)-2) + [Path.CLOSEPOLY]
    return PathPatch(Path(verts, codes), **kw) if verts else None

W, Sth, E, N = -5.0, 40.9, 17.0, 55.0
x0, y0, x1, y1 = proj(box(W, Sth, E, N)).bounds
x0 += 1.6e5; x1 -= 1.6e5; y1 -= 0.6e5
ratio = (y1 - y0) / (x1 - x0)
FW = 12; mapw = 0.94; maph = FW * mapw * ratio
FH = maph + 1.55
fig = plt.figure(figsize=(FW, FH), dpi=150)
fig.patch.set_facecolor("#f3ead6")
ax = fig.add_axes([0.03, 0.33 / FH, mapw, maph / FH])
ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="#c4d8de", edgecolor="#6b5e48", linewidth=1.2, zorder=0))
for g, fc, ec, lw in layers:
    if g.is_empty: continue
    p = patch(proj(g), facecolor=fc, edgecolor=ec, linewidth=lw, joinstyle="round", zorder=1)
    if p: ax.add_patch(p)
ax.add_patch(plt.Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor="none", edgecolor="#6b5e48", linewidth=1.2, zorder=5))
ax.set_xlim(x0, x1); ax.set_ylim(y0, y1); ax.set_aspect("equal"); ax.axis("off")
TITLE_Y = 1 - 0.62 / FH

def lab(lon, lat, txt, size=17, color="white", halo="#2f4a31", w="bold"):
    x, y = tr.transform(lon, lat)
    ax.text(x, y, txt, ha="center", va="center", fontsize=size, color=color, family=FONT, weight=w,
            linespacing=0.95, path_effects=[pe.withStroke(linewidth=3, foreground=halo)] if halo else None, zorder=10)

lab(2.4, 46.9, "Frankrike", 24, "#2b2724", "#d9d4cd")
lab(5.0, 52.35, "Nederländerna\n+ Belgien", 16)
lab(7.15, 50.65, "Preussen –\nRhenlandet", 15)
lab(8.15, 46.75, "Schweiz –\nneutralt", 15)
lab(8.15, 44.85, "Sardinien-Piemont\n+ Genua", 15)
lab(13.6, 52.75, "Preussen", 17, "#25402a", "#dfe8dc")
lab(10.6, 49.4, "Tyska stater –\nsplittrat", 17, "#3a3226", "#efe4c9")
lab(12.3, 42.6, "Italien –\nsplittrat", 17, "#3a3226", "#efe4c9")
lab(13.9, 47.35, "Österrike", 15, "#3a3226", "#efe4c9", "semibold")

fig.text(0.5, TITLE_Y, "Maktbalans: Frankrike omringas", ha="center", va="center", fontsize=34, family=FONT, weight="bold", color="#2b2724")
fig.text(0.97, 0.1 / FH, "Kartdata: historical-basemaps (A. Ourednik), Natural Earth", ha="right", va="bottom", fontsize=9, family=FONT, color="#7a6d58")
out = sys.argv[2]
fig.savefig(out, facecolor=fig.get_facecolor(), dpi=150)
print("ok", out)
