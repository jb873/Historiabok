# CLAUDE.md — Historiabok

> Designstandard och arbetsregler för Code när Code arbetar i 
> Historiabok-repot. Läs varje gång du startar en ny session.

**Senast uppdaterad:** 2026-06-15
**Plattformsversion:** Alphaskolans lärplattform v0.3 (Lager 1) + Lager 2-3-utökning v0.1
**Bok-status:** Nystartad. Medeltiden under produktion. Forntiden, Antiken, Upptäckterna, Vägen till första världskriget planeras.

---

## Vad detta repo är

Historiabok är **en av åtta böcker** i Alphaskolans lärplattform. Repot bygger på samma plattformsspec och samma komponentbibliotek som Geografiboken (jb873.github.io/Geografibok/), men med Historia-specifik identitet via accentfärger och kapitelstruktur.

**Repot är nystartat 2026-06-15.** Tidigare innehåll (Projekt 4: Revolutionernas tid, byggt under gammalt mönster) är arkiverat i branchen `v1-archive` och taggen `v1-arkiv-2026-06-15`. Det kommer återanvändas som källmaterial när Projekt 4 byggs om enligt nya mönstret — inte nu.

---

## Plattformen — vad är låst

### Fonter (LÅST på plattformsnivå)
- **Display/rubriker:** Marcellus SC
- **Brödtext:** EB Garamond
- Får ALDRIG ändras. Plattformsregeln är att eleven ska känna igen Alphaskolan omedelbart oavsett ämne.

### Bas-palett (LÅST)
- `--paper: #ece2c8`
- `--paper-light: #f4ecd6`
- `--ink: #1b2a36`
- `--brass: #b8902a` (motsvarar plattformens `--as-gold`)
- `--blood: #6e2e1e`
- `--terra: #b06a3a`
- `--land: #5e7a3e`
- `--ocean: #1e5c7a`
- `--muted: #6b5e4c`
- `--ink-blue: #4a6a85`

### Komponenter (LÅSTA mönster — kopiera från Geografi)
Följande komponenter implementeras enligt Geografibokens nu kanoniska mönster:
- `.flikar-rad` med fyra flikar: **Föreläsning** (ny standard), **Läs** (default), **Öva**, **Elevboken**
- `.bildguide` (brass-kant, 👁), `.karnpunkter` (terra-kant, 🎯), `.fordj-kort`, `.kort-grid`
- `.niva-valjare` med tre nivåer: 📗 Enkel / 📘 Standard (default) / 📕 Fördjupning
- `.underdel-valjare` (A/B/C/D inom Läs-fliken)
- `.begrepp-kort` med dynamisk upplåsning (8 ord, inga nyckelord)
- Elevbok med ramar i webben + print-CSS (16px webb, 11px print)
- Självskattning med fyra alternativ (Kan/Osäker/Kan ej/Ej bedömt), grupperade begreppsmoment, expandbara förtydliganden
- Export/Import via `elevdata-overforing.js`
- `.brodsmulor`, `.kapitel-kort`, `.resurs-kort`

**Hämta JS-modulerna från Geografi-repot:** elevbok.js, avsnitt-elevbok.js, begreppsbank.js, sjalvskattning-vy.js, elevdata-overforing.js, flipcards.js. Filerna är (eller blir) generaliserade till multiämnes-stöd. Behöver inte uppfinnas på nytt.

---

## Historia-specifikt

### Accentfärger (Historia-identitet)
Två färger utöver bas-paletten, definieras i `css/historia.css`:

```css
:root {
  --accent: #5a1a2a;     /* djup vinröd */
  --accent-2: #7a5a2e;   /* mörkt brons */
}
```

Inspirerat av medeltida illuminationer. Tonas mot manuskripts-känsla.

**Kapitelvariation:** Enskilda kapitel kan introducera **max 2 nya färger** som ämnesidentitet inom vintageatlas-ramverket. T.ex. Medeltiden kan ha sina egna nyanser. Beslutas per kapitel.

### Strukturhierarki
```
Historia (bok)
├── Medeltiden (kapitel)
│   ├── Tidig medeltid (delkapitel)
│   │   ├── Folkvandring (avsnitt)
│   │   ├── Kyrkans betydelse och utveckling (avsnitt)
│   │   └── ...
│   ├── Högmedeltiden (delkapitel)
│   └── Senmedeltiden (delkapitel)
├── Forntiden (kapitel, planeras)
├── Antiken (kapitel, planeras)
└── ...
```

### Filstruktur
```
Historiabok/
├── index.html                              ← bok-startsida
├── kapitel/
│   └── medeltiden/
│       ├── index.html                      ← kapitel-översikt
│       ├── delkapitel/
│       │   ├── tidig/
│       │   │   ├── index.html              ← delkapitel-översikt
│       │   │   ├── avsnitt-1-folkvandring.html
│       │   │   ├── avsnitt-2-kyrkans-betydelse.html
│       │   │   ├── ...
│       │   │   ├── djupdykning-1-...html
│       │   │   └── img/
│       │   ├── hog/
│       │   └── sen/
│       ├── data/
│       │   ├── fragor.json
│       │   ├── begreppsbank.json
│       │   ├── matris.json
│       │   └── flipcards/
│       │       ├── avsnitt-1-folkvandring.json
│       │       └── ...
│       ├── kapitelelevbok.html
│       ├── kapitelbegreppsbank.html
│       └── kapitelsjalvskattning.html
├── amneelevbok.html                        ← ämnesnivå
├── amnebegreppsbank.html
├── amnesjalvskattning.html
├── data/
│   └── delkapitel-lista.json
├── css/
│   ├── historia.css                        ← bok-override (accenter)
│   └── (delade plattformskomponenter)
├── js/
│   └── (delade plattformsmoduler)
├── CLAUDE.md                               ← denna fil
├── STATUS.md                               ← var står vi
└── TODO.md                                 ← nästa steg
```

### localStorage-prefix
Historia använder prefix `hist`. Exempel:
- `hist-elev-svar-{kapitel}`
- `hist-elev-begrepp-{kapitel}`
- `hist-elev-skattning`
- `hist-niva-{kapitel}-avsnitt-N`
- `hist-elev-identitet`

Geografi använder `geo` och delar inte data med Historia (separat scope i Export/Import).

### Klassnamn
Använd **flat naming** (samma som Geografi): `.elevbok-fraga-block`, `.begrepp-kort`, `.skatt-knapp`. BEM-migration är arbete för långt senare.

### Pedagogiska principer (samma som Geografi)
1. Packing-upp av kausala kedjor — INTE bullet-listor som dominerande format
2. Bildguider FÖRE bilder (advance organizer)
3. Djupdykningar i "Vill du veta mer?"-sektion längst ner i Läs-fliken (synliga oavsett underdelsval)
4. Differentiering: tre textnivåer per avsnitt
5. Stödord och startfraser på flipcards-redogörelsekort
6. Inga skuldläggningar — alltid positiv inramning

---

## Arbetsregler för Code

### Gör
- Kopiera kanoniska mönster från Geografi-repot rakt av
- Validera med `node --check` på alla JS
- Verifiera JSON är giltig
- Behåll print-CSS-mönstret från Geografi (`@media print`)
- Skriv `STATUS.md` och `TODO.md` när relevant — det är arbetsverktyg

### Gör INTE
- Uppfinn nya komponenter — om något saknas, **fråga ramverks-chatten** först
- Ändra plattformens fonter eller bas-palett
- Skapa parallella system till befintliga komponenter
- Hantera Projekt 4-migration (kommer senare, separat arbetsorder)
- Producera pedagogiskt innehåll (texter, frågor) — det gör innehållsproduktion-chatten
- Använd flat-naming där Geografi-versionen redan har BEM

### När du är osäker
1. Kolla först om Geografi-repot löst det
2. Kolla `PLATTFORMS-ANDRINGAR.md` om något är planerat att ändras
3. Fråga Joachim, som rådfrågar ramverks-chatten

---

## PLATTFORMS-ANDRINGAR.md
En instans av plattforms-ändringsdagboken ligger i repot. Observationer som påverkar plattformen läggs där, inte fixas direkt. Veckogenomgång på söndagar.

---

## Status och nästa steg
Se `STATUS.md` och `TODO.md` för aktuellt läge.

---

## Hänvisningar
- Plattformsspec Lager 1: `https://github.com/jb873/alphaskolans-larplattform/blob/v0.3/css/as-base.css`
- Lager 2-3-utökning: ramverks-chatten har originalet
- Geografi-repot (referens-implementation): `https://github.com/jb873/Geografibok`
