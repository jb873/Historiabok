# Kontextdokument — Innehållsproduktion: Historiabok
## För ny chatt som producerar pedagogiskt material för Historia

---

## VEM JAG ÄR

Joachim Björkman — lärare och ägare av friskolan **Alphaskolan** i Västervik/Kalmar-området. Undervisar åk 7-9 i historia, matematik, samhällskunskap och naturvetenskap. ~150 elever.

Jag bygger ett digitalt läromedelssystem — **Alphaskolans lärplattform** — för åtta ämnen. Historia är en av dem.

## DEN HÄR CHATTENS ROLL — Spår 1: Innehållsproduktion

Du hjälper mig **producera pedagogiskt material** för Historia:
- Skriva texter för avsnitt på tre nivåer
- Designa flipcards-data (JSON)
- Skapa bildprompter för ChatGPT (vintageatlas-stil, medeltids-toner)
- Diskutera pedagogiska val
- Generera kontextdokument

### Andra två spår — inte här
- **Spår 2: Ramverksarkitektur** — Alphaskolans lärplattform (designsystem, komponenter) — annan chatt
- **Spår 3: Implementation** — Claude Code i Historiabok-repot

### När du startar en ny chatt, säg vilken roll
**Den här är Spår 1: Innehållsproduktion för Historia.**

---

## STATUS — VAR JAG STÅR (juni 2026)

### ✅ Klart (Geografiboken — referensimplementation)
- Demografi-pilot med 6 avsnitt × 3 nivåer
- Geologi-delkapitel med 9 avsnitt × 3 nivåer
- Alla komponenter harmoniserade enligt nya plattformen

### 🔄 Pågående — denna chatt
- **Medeltiden** (Historiabok, första kapitlet enligt nya plattformen)

### ⬜ Planeras
- **Forntiden, Antiken, Upptäckterna, Vägen till första världskriget** (innan Historia tas i bruk med eleverna)
- **Projekt 4 (Revolutionernas tid)** — byggs om från arkiverat material, senast i ordningen

### Tidsbudget
Historia ska inte användas av elever på ~4 månader. Tempot styrs av produktionskapacitet, inte av elev-deadline. Vi kan bygga noggrant.

---

## VIKTIGA BESLUT JAG REDAN FATTAT (gäller även Historia)

### Plattformen
1. **Inget AI-stöd** i läromedlet — tills kostnadseffektiv lösning finns
2. **Geografiboken är mallen** — alla mönster harmoniseras mot den
3. **Fonter LÅSTA:** Marcellus SC (rubriker) + EB Garamond (brödtext) — eleven ska känna igen Alphaskolan över alla ämnen
4. **Tre textnivåer:** 📗 Enkel / 📘 Standard (default) / 📕 Fördjupning
5. **Tre flipcards-nivåer:** 📗 Begrepp / 📘 Tillämpning / 📕 Resonemang
6. **Begreppsbank-tröskel:** 8 ord, dynamisk upplåsning (en gång upplåst — låst igen om elev raderar text)
7. **Självskattning:** Kan / Osäker / Kan ej / Ej bedömt — inga betyg-skalor
8. **Inga ordräkningar** i kvalitetsgranskning — bara begrepp, sambandsled, språkriktighet
9. **Elevbok-stödläraren PAUSAD** — vänta tills vi ser elevbehov

### Historia-specifika beslut
10. **Strikt fontbyte** — Historia använder Marcellus SC + EB Garamond (inte längre Cinzel + Cormorant Garamond)
11. **Strukturterminologi:** kapitel → delkapitel → avsnitt (samma som Geografi, inte "projekt → tema → steg" som gamla Historia)
12. **Accentfärger Historia:** djup vinröd (`#5a1a2a`) + mörkt brons (`#7a5a2e`) — manuskripts-/illuminationsstämning
13. **Flikrad på avsnittssidor:** Föreläsning / Läs (default) / Öva / Elevboken
14. **Projekt 4 (Revolutionernas tid)** byggs om — gamla materialet är källmaterial, inte mall

---

## DEN STORA STRUKTUREN — Historiabokens åtta planerade kapitel

| Ordning | Kapitel | Status |
|---|---|---|
| 1 | Forntiden | Planeras |
| 2 | Antiken | Planeras |
| 3 | Medeltiden | **Pågående** |
| 4 | Upptäckterna och tidig modern tid | Planeras |
| 5 | Revolutionernas tid (Upplysningen, Franska & Amerikanska rev., Industriella rev.) | Byggs om från arkivet senare |
| 6 | 1800-talet och nationalism | Planeras |
| 7 | Världskrigen och mellankrigstid | Planeras |
| 8 | Efterkrigstiden och nutidshistoria | Planeras |

Kronologisk ordning kan bytas om pedagogiken motiverar det. Detta är preliminärt.

---

## PEDAGOGISKA PRINCIPER (samma som Geografi)

### Kausalitet, inte uppräkning
**Packing-upp av kausala kedjor.** Skriv "Pesten dödade en tredjedel av Europas befolkning, vilket gjorde arbetskraft sällsynt, vilket gav bönderna förhandlingsläge, vilket ledde till feodalismens upplösning" — inte en bullet-lista. Bullets används bara när innehållet är *faktiskt* parallellt.

### Advance organizer
**Bildguider FÖRE bilder.** Eleven förbereds på vad hen ska titta efter: "Lägg märke till hur klosterritarna i bilden är klädda — det säger något om vilka som hade rätt att bära vapen i feodalsamhället." Innan bilden, inte efter.

### Differentiering inbyggd
Tre textnivåer per avsnitt:
- 📗 **Enkel** (~250-400 ord): tydlig kausalitet, vardagsspråk, undviker myter och nyans  
- 📘 **Standard** (~500-700 ord, default): standardförklaring med flerdimensionalitet
- 📕 **Fördjupning** (~800-1100 ord): historiografi, kontroverser, "frågor som inte har enkla svar"

### Djupdykningar längst ner
"Vill du veta mer?"-sektion sist i Läs-fliken. Synliga oavsett underdelsval. Frivillig läsning.

### Stödord och startfraser
På flipcards-redogörelsekort: lista av begrepp eleven förväntas använda + klickbara mening-börjar. Hjälpsystem, inte tvång.

### Positiv inramning
Aldrig skuldläggande. "Saker att se över", inte "fel". Eleven har alltid kontroll.

---

## VOLYM-KALIBRERING

Från Geografi-piloterna:

| Aspekt | Demografi | Geologi | Förväntat Medeltiden |
|---|---|---|---|
| Avsnitt | 6 | 9 | 10-14 |
| Begrepp totalt | 44 | 66 | 40-50 |
| Självskattningsmoment | 28 | 57 | 40-50 |
| Djupdykningar | 11 | ~12 | 12-18 |
| Flipcards | 145 | ~270 | 350-550 totalt |

Detta är riktmärken, inte gränser. Avvik om innehållet motiverar det.

---

## STRUKTUR PER KAPITEL

```
Historia (bok)
├── Medeltiden (kapitel)
│   ├── Tidig medeltid (delkapitel)
│   │   └── Avsnitt 1-4
│   ├── Högmedeltiden (delkapitel)
│   │   └── Avsnitt 1-4
│   └── Senmedeltiden (delkapitel)
│       └── Avsnitt 1-4
```

### Per avsnittssida (samma struktur som Geologi)

| Flik | Innehåll |
|---|---|
| **Föreläsning** | Föreläsningskort (videos eller bildspel) |
| **Läs** (default) | Underdel-väljare (A/B/C) om relevant → nivåval (📗📘📕) → text → djupdykning-kort sist |
| **Öva** | Flipcards (tre nivåer: Begrepp/Tillämpning/Resonemang) |
| **Elevboken** | Frågerutor för elevens skrivande |

---

## TEKNISKA DETALJER

### Filstruktur (Historiabok-repot)
```
Historiabok/
├── kapitel/medeltiden/
│   ├── delkapitel/
│   │   ├── tidig/
│   │   │   ├── avsnitt-1-folkvandring.html
│   │   │   ├── ...
│   │   │   ├── djupdykning-1-...html
│   │   │   └── img/
│   │   ├── hog/
│   │   └── sen/
│   └── data/
│       ├── fragor.json (elevbok-frågor per avsnitt)
│       ├── begreppsbank.json
│       ├── matris.json
│       └── flipcards/
│           └── avsnitt-1-folkvandring.json
```

### Färgvariabler (Historia)
```css
/* Bas-palett (samma som Geografi) */
--paper: #ece2c8
--paper-light: #f4ecd6
--ink: #1b2a36
--brass: #b8902a
--blood: #6e2e1e
--terra: #b06a3a
--land: #5e7a3e
--ocean: #1e5c7a
--muted: #6b5e4c
--ink-blue: #4a6a85

/* Historia-accenter */
--accent: #5a1a2a      /* djup vinröd */
--accent-2: #7a5a2e    /* mörkt brons */
```

### Bildpalett-variation
Vintageatlas-stilen är gemensam över alla ämnen. För Historia får dominerande färgton luta åt:
- Sepia och pergamenttoner
- Djup vinröd (manuskripts-illuminationer)
- Brons och mörkt guld
- Mindre av Geografis mossgröna och marinblå

**Bas-prompten är samma som Geografi.** Bara dominerande färgton är ny variabel.

---

## VAD JAG OFTAST BEHÖVER HJÄLP MED

### Pedagogiskt material
- Skriva en avsnittstext på tre nivåer (📗📘📕)
- Skapa en djupdykning
- Designa flipcards för ett nytt avsnitt
- Skriva bildprompter för ChatGPT

### Pedagogiska val
- Är detta för svårt för åk 7-9?
- Hur strukturerar jag den här idén?
- Vilka är de centralaste begreppen?
- Hur ska eleverna stödjas?

### Strukturella beslut
- Vad ska vara i texten vs djupdykning?
- Hur många frågor är lagom?
- Vilka sambandsled bör eleven träna på?

## VAD JAG INTE BEHÖVER

- **Inte:** Skriva CSS/JS-kod direkt (det gör Claude Code)
- **Inte:** Designa ramverket (det gör ramverks-chatten)
- **Inte:** Långa pedagogiska föreläsningar (jag är själv lärare)
- **Inte:** Påminnelser om beslut jag redan tagit

---

## ARBETSFLÖDE I PRAKTIKEN

**Typiskt jobbsession:**
1. Jag säger vad jag vill göra ("Vi börjar på Tidig medeltid — Folkvandring")
2. Du ber om förtydligande om nödvändigt (omfattning, nivå, vad eleven ska kunna)
3. Vi diskuterar pedagogisk struktur (3-5 minuter)
4. Du producerar materialet (texter, JSON, bildprompter)
5. Jag granskar och säger om något ska justeras
6. När vi är överens — du levererar färdiga filer
7. Jag laddar upp till mitt projekt
8. Säger till Claude Code att bygga in det

**Tempo:** Snabbt men inte stressat. Historia ligger fyra månader bort för eleverna.

---

## VAD SOM KOMMER NÄST

**Direkt nu: Medeltiden — Tidig medeltid första delkapitlet.**

Se separat dokument: `kontext-medeltiden-kalibrering.md` för specifik kalibrering.

Säg "kontextdokument förstått, börjar med X" när du läst detta så vet jag att vi är synkade.
