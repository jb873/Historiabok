# Arbetsorder — Vägen till första världskriget: Wienkongressen 1814–1815

**Repo:** Historiabok · **Datum:** 2026-10-24
**Styrdokument (läs FÖRE all HTML):** `doc/KOMPONENTER-INNEHALL-HISTORIA` v1.10 · `doc/LEVERANSGUIDE-INNEHALL` v2.1
**Mall att följa:** avsnittssidan `avsnitt-1-nationalism.html` i delkapitlet `ideologier`, som byggdes och godkändes i förra ordern. Samma struktur, samma komponenter, samma sätt att generera sidan från innehållsfilerna.

---

## 0. Beslut som Joachim bekräftar innan ordern skickas

| Vad | Förslag |
|---|---|
| Delkapitel-id / mapp | `wienkongressen` |
| Delkapiteltitel | Wienkongressen och den nya ordningen |
| Avsnittsfil | `avsnitt-1-wienkongressen.html` |
| `AVSNITT_ID` | `a1_wienkongressen` |
| Avsnittstitel | Wienkongressen |
| Hero-subtitel | — freden som skulle bevara det gamla Europa — |
| `ar` i avsnittslistan | `1814-1815` |
| `data-niva-nyckel` | `hist-niva-vagen-till-forsta-varldskriget-wienkongressen` |

Bakgrund: Joachim har börjat om med 1800-talet och lägger Wienkongressen först, före ideologierna. Delkapitlet `ideologier` och avsnittet om nationalism **rörs inte** i denna order. De byggs om i en senare order.

---

## 1. Syfte

Bygga avsnittssidan för Wienkongressen med fyra underdelar i tre nivåer, fyra bilder och delkapitlets avsnittslista. Inget annat.

**Ingår INTE** (kommer senare): flipcards, begreppsbank, matris, frågor till Elevboken (Joachim skriver dem själv), föreläsningar, djupdykningar, kapitel- och delkapitellandning, ändringar i `ideologier`.

---

## 2. Leverans

Lägg hela leveransen i `doc/leveranser/vtfvk-wienkongressen/` och committa den. Innehåll:

| Mapp | Innehåll |
|---|---|
| `innehall/` | En fil per underdel (A–D) med BILD-block, Enkel (kärnpunkter, bildguide, brödtext), Standard och Fördjupning |
| `img/` | De fyra bilderna, filnamn exakt som levererade |
| `versioner/` | Tidigare versioner av texter och bilder. Bara arkiv, används inte i bygget |
| `kartverktyg/` | Skriptet som ritade kartan i C. Bara arkiv, används inte i bygget |

---

## 3. Arbetsgång

### Steg 1: Inventera och rapportera (bygg inget ännu)

1. Bekräfta att `kapitel/vagen-till-forsta-varldskriget/data/` finns och vad den innehåller i dag.
2. Hur hanterar `avsnitt-elevbok.js` ett avsnitt vars id inte finns i `fragor.json`? Felmeddelande, tom flik eller konsolfel?
3. Bekräfta att mönstret från nationalismsidan (sökvägar, `data-fil`, brödsmulor, bildernas relativa sökväg `img/…`) kan återanvändas rakt av.

Vänta på godkännande innan steg 2.

### Steg 2: Bygg

Skapa, utan att röra befintliga filer och utan att röra `Arkiv/`:

1. `kapitel/vagen-till-forsta-varldskriget/delkapitel/wienkongressen/img/` med de fyra bilderna.
2. `kapitel/vagen-till-forsta-varldskriget/delkapitel/wienkongressen/avsnitt-1-wienkongressen.html`.
3. `kapitel/vagen-till-forsta-varldskriget/data/avsnittslista-wienkongressen.json` (se avsnitt 5).

Git-commit per steg.

---

## 4. Avsnittssidan

Följ KOMPONENTER DEL 1 och nationalismsidan. Ändra aldrig klassnamn, elementtyper eller nesting.

### Header
- Tidslinje-header med `data-fil="../../data/avsnittslista-wienkongressen.json"`.
- Brödsmulor: Historia › Vägen till första världskriget › Wienkongressen och den nya ordningen › Wienkongressen. Länkarna följer mönstret även om landningssidorna inte finns än.
- `avsnitt-label` = `Avsnitt 1`, `h1` = Wienkongressen, subtitel enligt tabellen i 0.

### Flikar
Som på nationalismsidan. Öva: flipcards-mount med `data-fil="../../data/flipcards/avsnitt-1-wienkongressen.json"` och `data-avsnitt="a1_wienkongressen"` (filen finns inte än).

### Läs-fliken

| Bokstav | `data-underdel` | Titel | Innehållsfil |
|---|---|---|---|
| A | `a` | Europa efter Napoleon | `innehall/A-europa-efter-napoleon.md` |
| B | `b` | Återställa det gamla Europa | `innehall/B-aterstalla-det-gamla-europa.md` |
| C | `c` | Maktbalans – Europas nya karta | `innehall/C-maktbalans-europas-nya-karta.md` |
| D | `d` | En ordning som utmanas | `innehall/D-en-ordning-som-utmanas.md` |

Översättning från innehållsfilerna, samma regler som för nationalismsidan:
- **Standard:** `**Inledning**` blir `<p class="inledning">`. Rubriker `###` blir `<h2>`. På raden `[BILD HÄR]`: `<figure class="brodtext-bild standard">` med fil, alt-text och Standard-bildtexten från filens BILD-block.
- **Enkel:** först `.karnpunkter`, sedan brödtexten. På raden `[BILDGUIDE + BILD HÄR]`: `.bildguide` med punkterna under "Bildguide", följd av `<figure class="brodtext-bild enkel">` med **samma fil och alt-text** och Enkel-bildtexten.
- **Fördjupning:** rubriker `###` blir `<h2>`, ingen bild.
- Rubrikraderna "Kärnpunkter", "Bildguide" och "Brödtext" är sorteringsetiketter och ska inte synas på sidan. Rader som "Versioner:" och "Ändring v2 → v3:" är anteckningar och ska inte heller synas.
- Ingen djupdykningssektion.

### Script-block
```
const AVSNITT_ID = 'a1_wienkongressen';
const KAPITEL_ID = 'vagen-till-forsta-varldskriget';
const DELKAPITEL_ID = 'wienkongressen';
```

---

## 5. Avsnittslistan

```json
{
  "delkapitel": "wienkongressen",
  "delkapitel_titel": "Wienkongressen och den nya ordningen",
  "kapitel": "vagen-till-forsta-varldskriget",
  "avsnitt": [
    {
      "id": "a1_wienkongressen",
      "nummer": 1,
      "titel": "Wienkongressen",
      "ar": "1814-1815",
      "fil": "avsnitt-1-wienkongressen.html"
    }
  ]
}
```

---

## 6. Verifiering (headless Chromium)

1. Sidan laddar utan konsolfel, utöver förväntade fel för saknade datafiler (lista dem separat).
2. Alla 12 kombinationer underdel × nivå visar rätt text, bara en åt gången.
3. `#a`–`#d` öppnar rätt underdel.
4. Alla fyra bilder laddar på Enkel och Standard (`naturalWidth > 0`), samma fil och alt-text på båda, ingen bild på Fördjupning.
5. Kärnpunkter och bildguide syns bara på Enkel.
6. Inga anteckningsrader ("Versioner:", "Ändring", "Kärnpunkter", "Brödtext") syns på sidan.
7. Tidslinjen visar "Du är här" på Wienkongressen 1814-1815.
8. Skärmdumpar: Standard A, Enkel C, Fördjupning D.

---

## 7. Ramar

Återanvänd komponenter, bygg inga nya. Gissa aldrig, fråga. Skriv inte över befintliga filer. Rör inte `Arkiv/` och inte delkapitlet `ideologier`. Filnamn är skiftlägeskänsliga.
