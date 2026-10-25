# Arbetsorder — Vägen till första världskriget: Politiska ideologier

**Repo:** Historiabok · **Datum:** 2026-10-25
**Styrdokument (läs FÖRE all HTML):** `doc/KOMPONENTER-INNEHALL-HISTORIA` v1.10 (DEL 1 avsnitt, DEL 4.1 fordj-kort, DEL 8 djupdykning) · `doc/LEVERANSGUIDE-INNEHALL` v2.1
**Mall:** `delkapitel/wienkongressen/avsnitt-1-wienkongressen.html` och generatorn som byggde den.

*(Arbetsordern levererades som inklistrad text, inte i zip-filen. Sparad här ordagrant i sak.)*

## 0. Beslut som Joachim bekräftar innan ordern skickas

| Vad | Förslag |
|---|---|
| Placering | Avsnitt 2 i delkapitlet `wienkongressen`, direkt efter Wienkongressen |
| Avsnittsfil | `avsnitt-2-politiska-ideologier.html` |
| `AVSNITT_ID` | `a2_politiska-ideologier` |
| Avsnittstitel | Politiska ideologier |
| Hero-label | Avsnitt 2 |
| Hero-subtitel | — tre svar på frågan hur samhället ska styras — |
| `ar` i avsnittslistan | `1815-1900` |
| `data-niva-nyckel` | `hist-niva-vagen-till-forsta-varldskriget-politiska-ideologier` |

Varför i `wienkongressen`: Wienkongressens avsnitt slutar med frågan "Hur ska det nya samhället styras?", och ideologierna är svaret. Delkapitlet heter "Wienkongressen och den nya ordningen", och ideologierna är de idéer som utmanade ordningen. Placeringen kräver ingen omnumrering. Det publicerade avsnittet `a1_nationalism` i `ideologier` rörs inte. Nationalism (och senare feminism) byggs om i en egen order.

Om Joachim hellre vill lägga avsnittet i `ideologier`: stoppa och rapportera, eftersom det kräver omnumrering av den publicerade nationalismsidan och dess data.

## 1. Syfte

Bygga avsnittssidan Politiska ideologier med tre underdelar i tre nivåer, tre djupdykningssidor och en uppdaterad avsnittslista.

**Ingår INTE:** bilder (kommer senare), flipcards, begreppsbank, matris, elevboksfrågor (Joachim skriver dem), föreläsningar, ändringar i Wienkongressens avsnitt 1 eller i delkapitlet `ideologier`.

## 2. Leverans

Lägg hela leveransen i `doc/leveranser/vtfvk-politiska-ideologier/` och committa.

| Mapp | Innehåll |
|---|---|
| `innehall/` | `A-konservatism.md`, `B-liberalism.md`, `C-socialism.md`, var och en med Enkel (kärnpunkter + brödtext), Standard och Fördjupning |
| `djupdykningar/` | `djupdykning-burke-mot-paine.md`, `djupdykning-aftonbladet-och-kungen.md`, `djupdykning-karl-marx-och-historien.md` |
| `standard-txt/` | Standardtexterna som rena textfiler. Bara arkiv |
| `versioner/` | ChatGPT-originalen (Standard v1). Bara arkiv |

## 3. Arbetsgång

### Steg 1: Inventera och rapportera (bygg inget ännu)
1. Hanterar generatorn innehållsfiler utan BILD-block och utan bildguide? Raden "Bild och bildguide läggs till när bilden är gjord." är en anteckning och ska inte synas.
2. Fungerar avsnittssidan med tre underdelar (A–C) i stället för fyra?
3. Djupdykningar: Titta på hur befintliga djupdykningssidor i boken är byggda, till exempel Medeltidens "En bondflicka som ändrade ett krig" och Reformationens. Rapportera hur de hanterar inledningen (motsvarar blocket `## Tema`), slutet (motsvarar blocket `## Koppling till avsnittet`) och ikonen i fordj-kort (vilken praxis boken har). Föreslå hur mina block ska översättas så att de följer samma mönster. Gissa inte.
4. Hur ser avsnittslistan `avsnittslista-wienkongressen.json` ut i dag, och visar tidslinjen två avsnitt utan problem?

Vänta på godkännande innan steg 2.

### Steg 2: Bygg
1. `delkapitel/wienkongressen/avsnitt-2-politiska-ideologier.html`, genererad från innehållsfilerna.
2. Tre djupdykningssidor enligt KOMPONENTER DEL 8 i samma mapp.
3. Ny post i `kapitel/vagen-till-forsta-varldskriget/data/avsnittslista-wienkongressen.json` (se avsnitt 6).

Git-commit per steg.

## 4. Avsnittssidan

Samma struktur som Wienkongressens avsnitt 1.

Brödsmulor: Historia › Vägen till första världskriget › Wienkongressen och den nya ordningen › Politiska ideologier.

Öva: `data-fil="../../data/flipcards/avsnitt-2-politiska-ideologier.json"`, `data-avsnitt="a2_politiska-ideologier"` (finns inte än).

| Bokstav | `data-underdel` | Titel | Innehållsfil |
|---|---|---|---|
| A | `a` | Konservatism | `innehall/A-konservatism.md` |
| B | `b` | Liberalism | `innehall/B-liberalism.md` |
| C | `c` | Socialism | `innehall/C-socialism.md` |

Översättningsreglerna är desamma som tidigare. Skillnader:
- Enkel börjar med ett inledningsstycke före första `###`-rubriken. Det blir vanlig `<p>` (inte `inledning`) efter kärnpunkterna.
- Standard har `**Inledning**` som blir `<p class="inledning">`.
- Rubriken "Tre olika svar" i C är en vanlig `<h2>` på alla nivåer där den finns.
- Kärnord som BEVARA, FRIHET och JÄMLIKHET står med versaler i fetstil och ska behållas så.

### Djupdykningssektionen (DEL 4.1)

| Kort | href | Titel | Sammanfattning |
|---|---|---|---|
| 1 | `djupdykning-burke-mot-paine.html` | Burke mot Paine – pennkriget om franska revolutionen | Två vänner blev bittra fiender när de skrev om franska revolutionen. Deras böcker blev startskottet för konservatism och liberalism. |
| 2 | `djupdykning-aftonbladet-och-kungen.html` | Aftonbladet och kungen – kampen för tryckfriheten i Sverige | Varje gång regeringen stängde Aftonbladet startade Lars Johan Hierta en ny tidning med nästan samma namn. Så vann tryckfriheten i Sverige. |
| 3 | `djupdykning-karl-marx-och-historien.html` | Karl Marx – historien sedd genom ekonomin | En landsflyktig tysk i London ville förklara hela historien. Hans idé om att ekonomin formar samhället påverkar fortfarande hur historiker arbetar. |

### Script-block
```
const AVSNITT_ID = 'a2_politiska-ideologier';
const KAPITEL_ID = 'vagen-till-forsta-varldskriget';
const DELKAPITEL_ID = 'wienkongressen';
```

## 5. Djupdykningssidorna (DEL 8)

| Fil | Tillbaka-länk | Brödsmula 5 | Subtitel |
|---|---|---|---|
| `djupdykning-burke-mot-paine.html` | `avsnitt-2-politiska-ideologier.html#a` | 2. Politiska ideologier | — två vänner, två böcker, två ideologier — |
| `djupdykning-aftonbladet-och-kungen.html` | `avsnitt-2-politiska-ideologier.html#b` | 2. Politiska ideologier | — tidningen som inte gick att stänga — |
| `djupdykning-karl-marx-och-historien.html` | `avsnitt-2-politiska-ideologier.html#c` | 2. Politiska ideologier | — en teori om vad som driver historien — |

- `h1` = titeln efter "Djupdykning:" i filens första rad.
- Brödtext: rubriker `###` under `## Text` blir `<h2>` och stycken blir `<p>`. Kursiv (`*…*`) blir `<em>`, fetstil blir `<strong>`.
- Rader överst (`**Fil:**`, `**Kort (fordj-kort):**`) och rubriken `## Text (~… ord)` är anteckningar och ska inte synas.
- `## Tema` och `## Koppling till avsnittet`: enligt det mönster du rapporterar i steg 1.
- Bottenlänk `<p class="tillbaka-lank">` till samma ankare som den sticky tillbaka-länken.
- Bara `elevfeedback.js` laddas.

## 6. Avsnittslistan

Lägg till efter `a1_wienkongressen`:

```json
{
  "id": "a2_politiska-ideologier",
  "nummer": 2,
  "titel": "Politiska ideologier",
  "ar": "1815-1900",
  "fil": "avsnitt-2-politiska-ideologier.html"
}
```

## 7. Verifiering (headless Chromium)
1. Avsnittssidan laddar utan konsolfel, utöver förväntade 404 för flipcards och föreläsningar.
2. Alla 9 kombinationer underdel × nivå visar rätt text, bara en åt gången. `#a`–`#c` öppnar rätt underdel.
3. Kärnpunkter syns bara på Enkel. Inga bilder, ingen bildguide och inga anteckningsrader syns.
4. Tidslinjen visar två avsnitt med "Du är här" på rätt avsnitt, både på avsnitt 1 och avsnitt 2.
5. De tre djupdykningskorten länkar rätt. Varje djupdykningssida har rätt tillbaka-länk (sticky och botten) till rätt underdel, och brödsmulorna stämmer.
6. Wienkongressens avsnitt 1 och nationalismsidan är oförändrade (diff).
7. Skärmdumpar: Standard A, Enkel C (med "Tre olika svar") och en djupdykningssida.

## 8. Ramar

Återanvänd komponenter, bygg inga nya. Gissa aldrig, fråga. Skriv inte över befintliga filer. Rör inte `Arkiv/` eller delkapitlet `ideologier`. Vänta med push tills Joachim säger till.

---

## Joachims beslut efter steg 1 (2026-10-25)
- Generatorn: tillåt noll bilder och lägg till `*…*` → `<em>`. Kontrollera att Nationalism- och Wienkongressen-sidorna fortfarande byggs identiskt.
- `## Tema` blir inledande stycken utan rubrik; `## Koppling till avsnittet` visas inte.
- Fotnot: `<p class="footnote">Historia · Vägen till första världskriget</p>`.
- Ikoner: 🖋️ Burke mot Paine, 📰 Aftonbladet och kungen, 🏭 Karl Marx.
- Fyndet om de tre Reformationssidorna loggas i PLATTFORMS-ANDRINGAR som separat rättelse.
- Vänta med push.
