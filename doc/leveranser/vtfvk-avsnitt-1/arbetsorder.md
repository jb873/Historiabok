# Arbetsorder — Vägen till första världskriget, avsnitt 1: Nationalism

**Repo:** Historiabok · **Datum:** 2026-09-27
**Styrdokument (läs FÖRE all HTML):** `doc/KOMPONENTER-INNEHALL-HISTORIA` v1.10 · `doc/LEVERANSGUIDE-INNEHALL` v2.1

---

## 0. Beslut som bekräftas av Joachim innan ordern skickas

| Vad | Förslag |
|---|---|
| Kapitel-id / mapp | `vagen-till-forsta-varldskriget` |
| Kapiteltitel | Vägen till första världskriget |
| Delkapitel-id / mapp | `ideologier` |
| Delkapiteltitel | Ideologiernas århundrade |
| Avsnittsfil | `avsnitt-1-nationalism.html` |
| `AVSNITT_ID` | `a1_nationalism` |
| Avsnittstitel | Nationalism |
| Hero-subtitel | — idén som ritade om Europas karta — |
| `ar` i avsnittslistan | `1815-1871` |

Delkapitlet får två avsnitt (avsnitt 2: Liberalism, konservatism och socialism byggs senare).

---

## 1. Syfte

Bygga avsnittssidan för avsnitt 1 (Nationalism) med fyra underdelar i tre nivåer, fyra bilder och delkapitlets avsnittslista. Inget annat.

**Ingår INTE i denna order** (kommer i senare leveranser): flipcards, begreppsbank, frågor, matris, föreläsningar, djupdykningar, avsnitt 2, kapitelstartsida och delkapitel-landning.

---

## 2. Arbetsgång — inventera först, bygg sedan

### Steg 1: Inventera och rapportera (bygg inget ännu)

Rapportera till Joachim:

1. Finns kapitelmappen redan? Finns `kapitel/{kapitel}/index.html`, `data/` och kapitelverktygen?
2. **Sökvägen till avsnittslistan.** KOMPONENTER DEL 1 anger `data-fil="../../data/avsnittslista-{delkapitel}.json"` (kapitlets data-mapp), men LEVERANSGUIDE DEL 7 anger `kapitel/{kapitel}/delkapitel/{delkapitel}/data/avsnittslista.json`. Kontrollera vad befintliga kapitel (t.ex. Revolutionernas tid eller Medeltiden) faktiskt använder och vad `js/tidslinje.js` läser. Gissa inte.
3. `data-niva-nyckel`: vilket prefix använder befintliga avsnitt? Mönstret är `{prefix}-niva-{kapitel}-{slug}`.
4. Hur hanterar `flipcards.js` och `avsnitt-elevbok.js` att datafilerna saknas? Blir det felmeddelande, tom flik eller konsolfel?
5. Var ligger `img/` för befintliga delkapitel, och vilken sökväg använder deras `<img src>`?

Vänta på godkännande innan steg 2.

### Steg 2: Bygg

Skapa följande, utan att röra befintliga filer och utan att röra `Arkiv/`:

1. `kapitel/{kapitel}/delkapitel/{delkapitel}/img/` med de fyra bilderna från leveransens `img/` (filnamn exakt som levererade, skiftlägeskänsligt).
2. `kapitel/{kapitel}/delkapitel/{delkapitel}/avsnitt-1-nationalism.html` enligt KOMPONENTER DEL 1 (se avsnitt 3 nedan).
3. Avsnittslistan på den plats inventeringen visar är rätt (se avsnitt 4).

Git-commit per steg.

---

## 3. Avsnittssidan

**Mall:** KOMPONENTER DEL 1, kopierad rakt av. Ändra aldrig klassnamn, elementtyper eller nesting.

### Header
- Tidslinje-header: med, `data-fil` enligt inventeringen.
- Hero-banner: brödsmulor Historia › Vägen till första världskriget › Ideologiernas århundrade › Nationalism. `avsnitt-label` = `Avsnitt 1`. `h1` = Nationalism. Subtitel enligt tabellen i 0.

### Flikar
- Föreläsning: tom `.forelasningar-lista` (ingen JSON ännu, fliken blir disabled).
- Läs: se nedan.
- Öva: flipcards-mount med `data-fil="../../data/flipcards/avsnitt-1-nationalism.json"` och `data-avsnitt="a1_nationalism"`. Filen finns inte än, rapportera beteendet.
- Elevboken: standardmount.

### Läs-fliken
**Underdelsväljare**, fyra knappar:

| Bokstav | `data-underdel` | Titel | Innehållsfil |
|---|---|---|---|
| A | `a` | Ett folk – ett land | `innehall/1A-ett-folk-ett-land.md` |
| B | `b` | Splittra eller förena | `innehall/1B-splittra-eller-forena.md` |
| C | `c` | Italien enas | `innehall/1C-italien-enas.md` |
| D | `d` | Tyskland enas | `innehall/1D-tyskland-enas.md` |

**En** delad `.niva-valjare` efter underdelsväljaren, utanför alla `.underdel-text`.

**Per underdel**, tre `.niva-innehall brodtext`-block (Enkel och Fördjupning med `dold`, Standard utan):

- **Standard:** `**Inledning**` → `<p class="inledning">`. Rubriker `###` → `<h2>`. Stycken → `<p>`. Fetstil → `<strong>`. Bilden som `<figure class="brodtext-bild standard">` på raden `[BILD HÄR]`, med alt-text och Standard-bildtexten från filens BILD-block.
- **Enkel:** först `.karnpunkter` (h3 "🎯 Kärnpunkter", punkterna under "Kärnpunkter" i filen). Sedan brödtexten, rubriker `###` → `<h2>`. På raden `[BILDGUIDE + BILD HÄR]`: `.bildguide` (h3 "👁 Titta efter", punkterna under "Bildguide") följt av `<figure class="brodtext-bild enkel">` med **samma src och alt** som Standard och Enkel-bildtexten.
- **Fördjupning:** rubriker `###` → `<h2>`, ingen bild.

Rubrikraderna "Kärnpunkter", "Bildguide" och "Brödtext" i innehållsfilerna är sorteringsetiketter och ska inte synas på sidan.

**Djupdykningar:** utelämna hela `<section class="djupdykningar">` tills djupdykningarna finns.

### Script-block
```
const AVSNITT_ID = 'a1_nationalism';
const KAPITEL_ID = 'vagen-till-forsta-varldskriget';
const DELKAPITEL_ID = 'ideologier';
```
Därefter scripten i exakt den ordning KOMPONENTER DEL 1 anger.

---

## 4. Avsnittslistan (LEVERANSGUIDE DEL 7)

```json
{
  "delkapitel": "ideologier",
  "delkapitel_titel": "Ideologiernas århundrade",
  "kapitel": "vagen-till-forsta-varldskriget",
  "avsnitt": [
    {
      "id": "a1_nationalism",
      "nummer": 1,
      "titel": "Nationalism",
      "ar": "1815-1871",
      "fil": "avsnitt-1-nationalism.html"
    }
  ]
}
```

`id` måste matcha `AVSNITT_ID` exakt.

---

## 5. Verifiering (headless Chromium, inte node-harness)

Puppetera publika kontroller och rapportera:

1. Sidan laddar utan konsolfel (utöver förväntade fel för saknade JSON-filer, som ska listas separat).
2. Alla 12 kombinationer underdel × nivå visar rätt text, och bara en åt gången.
3. `#a`, `#b`, `#c`, `#d` i URL:en öppnar rätt underdel.
4. Alla fyra bilder laddar på både Enkel och Standard (kontrollera `naturalWidth > 0`), och ingen bild finns på Fördjupning.
5. Bildguide och kärnpunkter syns bara på Enkel.
6. Tidslinje-headern renderar och markerar avsnitt 1 som "Du är här".
7. Hero-bannern visar fyra brödsmulor, där sista inte är klickbar.
8. Skärmdumpar: Standard A, Enkel B, Fördjupning D, samt mobilbredd 390 px.

---

## 6. Ramar

- Återanvänd komponenter, bygg inga nya.
- Gissa aldrig struktur. Är något oklart: fråga.
- Skriv aldrig över befintliga filer. `Arkiv/` rörs inte.
- Filnamn skiftlägeskänsliga (Pages/Linux).

---

## 7. Kanoniseringsnot (för ramverkschatten, ej denna order)

Delkapitel- och kapitellandning byggs i senare order. När de byggs gäller direktlänk-regeln och ingress-på-flerradiga-landningar (🟡 beslutade). VTFVK är utpekat som trigger för att kanonisera dem i KOMPONENTER — meddela ramverkschatten när mönstret satt sig.

---

## Tillägg vid godkännande av steg 1 (Joachim, 2026-09-27)

- Avsnittslistan läggs i `kapitel/vagen-till-forsta-varldskriget/data/avsnittslista-ideologier.json`; `data-fil` följer befintligt mönster. Rättelsen av LEVERANSGUIDE DEL 7 loggas i PLATTFORMS-ANDRINGAR.md.
- `data-niva-nyckel="hist-niva-vagen-till-forsta-varldskriget-nationalism"`.
- Leveransen läggs i `doc/leveranser/vtfvk-avsnitt-1/` och committas.
- Brödsmulorna följer mönstret redan nu (landningssidorna kommer i nästa order).
- `data/delkapitel-lista.json` rörs inte.
