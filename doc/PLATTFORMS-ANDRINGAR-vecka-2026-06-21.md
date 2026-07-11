# Veckogenomgång 2026-06-21 — beslut att logga

> Dessa poster läggs in i den befintliga `PLATTFORMS-ANDRINGAR.md` 
> (både i Historiabok-repot och Geografibok-repot eftersom delade 
> komponenter påverkas).

**Datum för veckogenomgång:** Lördag 2026-06-21
**Trigger:** Eleverfeedback efter testkörning + kollegafeedback från webbdesigner
**Format:** Tre observationskällor (elever, kollega, Joachim) sorterade till handlingsplan

---

## 🟢 Implementerade (efter Code är klar)

### 2026-06-21 — Brödtext 16→17px

| Fält | Värde |
|---|---|
| Typ | C (plattformsmodell — Lager 1-justering) |
| Var upptäckt | Eleverfeedback efter testkörning |
| Observation | Elever rapporterar att brödtexten är för liten på Chromebook 1366×768. Vissa zoomar för att kunna läsa. |
| Beslut | Höj bas-font till 17px i `css/geografi.css`. Print-CSS oförändrad (11px). |
| Status | 🟢 Implementerad, väntar verifiering |
| Berör | Båda repon (delad CSS) |

### 2026-06-21 — KOMPONENTER-INNEHALL.md v1.2

| Fält | Värde |
|---|---|
| Typ | C (dokumentation) |
| Var upptäckt | Joachim levererade scaffold-mall efter buggar i Medeltids-bygget |
| Observation | Avsnitts-scaffolden (flik/nivå/underdel-strukturen) och brödtext-principerna per nivå var inte dokumenterade. Innehållssessioner och Code uppfann eller missuppfattade strukturen. |
| Beslut | KOMPONENTER-INNEHALL v1.2 levererad med tre nya delar: avsnitts-scaffold + brödtext-principer per nivå + bildstöd-mönstret per nivå. |
| Status | 🟢 Implementerad — finns i `doc/` i båda repon |
| Berör | Alla framtida innehållsproduktion (alla böcker) |

---

## 🟡 Beslutade, väntar implementation

### 2026-06-21 — Kontrast-inventering paper/ink

| Fält | Värde |
|---|---|
| Typ | C (plattformsmodell) |
| Var upptäckt | Eleverfeedback — texten "smälter ihop med bakgrunden" |
| Observation | Möjliga problem: brödtext mot `--paper`, sekundärtext i `--muted` mot `--paper`, text på `--paper-light`-ytor. |
| Beslut | Code inventerar WCAG-kontrasträtio för alla färgkombinationer. Rapporterar tillbaka. Joachim väljer åtgärd. |
| Status | 🟡 Code arbetar med inventering |
| Berör | Båda repon |

### 2026-06-21 — Sidobreddsinventering

| Fält | Värde |
|---|---|
| Typ | B (mönster) |
| Var upptäckt | Eleverfeedback — "mycket tomrum på båda sidorna" |
| Observation | `.sida` har förmodligen `max-width` runt 900-1100px. På Chromebook 1366×768 ger det stora marginaler. |
| Beslut | Code inventerar nuvarande `max-width` på `.sida` och `.brodtext`. Föreslår tre alternativ. Joachim väljer. **Princip:** brödtext-rader ska inte bli längre än 60-75 tecken även om container utvidgas. |
| Status | 🟡 Code arbetar med inventering |
| Berör | Båda repon |

### 2026-06-21 — Rubrik-synlighet

| Fält | Värde |
|---|---|
| Typ | B (mönster) |
| Var upptäckt | Kollegafeedback (webbdesigner) |
| Observation | Marcellus SC-rubriker syns inte tillräckligt distinkt i layouten. |
| Beslut | Code inventerar nuvarande font-size, font-weight, letter-spacing för h1-h3. Föreslår subtila justeringar utan att byta font (Marcellus SC är låst). Joachim väljer. |
| Status | 🟡 Code arbetar med inventering |
| Berör | Båda repon |

### 2026-06-21 — Sektionsmarkering (inneslutningsprincipen)

| Fält | Värde |
|---|---|
| Typ | B (mönster) |
| Var upptäckt | Kollegafeedback — "streck eller kontrast" |
| Observation | Vissa sektionsgränser kan vara otydliga (h2-sektioner i brödtext, mellan flikar). |
| Beslut | Code föreslår tre konkreta platser där subtil sektionsmarkering skulle göra störst skillnad. Joachim väljer 0-3 att implementera. **Princip:** subtilt, vintageatlas-paletten ska inte brytas. |
| Status | 🟡 Code arbetar med förslag |
| Berör | Båda repon |

---

## 🔵 Parkerade — Omgång 2

### 2026-06-21 — Sticky header med minimering

| Fält | Värde |
|---|---|
| Typ | B (mönster) |
| Var upptäckt | Kollegafeedback — "header som följer med och minimeras" |
| Observation | Vertikal yta på Chromebook 1366×768 är knapp. Sticky-element tar plats. |
| Beslut | **Parkerad** tills Omgång 1 har visat effekt hos eleverna. Om eleverna fortfarande har navigations-problem efter Omgång 1 — då tar vi upp detta igen med prototyp + elev-test. |
| Status | 🔵 Att bedöma efter Omgång 1 |

### 2026-06-21 — Designprinciper för djupare omarbetning

Kollegan nämnde flera designlagar (närhetens lag, likhetens lag, slutenhetens lag). Inneslutningsprincipen är delvis adresserad i 🟡-listan ovan. Övriga principer är värdefulla men ej akuta.

Status: 🔵 Att bedöma om eleverna fortfarande har orienterings-problem efter Omgång 1.

---

## ❌ Förkastade

### 2026-06-21 — Tvåspaltsupplägg med elevbok/begreppsbank/matris i sidospalt

| Fält | Värde |
|---|---|
| Typ | B (mönster) |
| Var upptäckt | Kollegafeedback — "två spalter med viktiga resurser i sidan" |
| Observation | Förslag att elevbok, begreppsbank och matris syns alltid i sidospalt på avsnittssidor. |
| Beslut | **Förkastat.** Skäl: bryter den medvetna flikseparationen (Föreläsning/Läs/Öva/Elevboken) som etablerats för att skilja aktiviteter åt. Elevboken är aktivt skrivande — inte en passiv referens. Att lyfta in den i sidospalt blandar arbetstyperna. Eleven har redan tillgång via flikraden. |
| Status | ❌ Förkastat |

---

## Process — denna veckogenomgång

För framtida veckogenomgångar — så här fungerade det:

1. **Joachim samlade observationer från flera källor:** elever (testkörning), kollega (webbdesigner), egna pedagogiska beslut
2. **Ramverks-chatten sorterade** observationer per typ (A/B/C) och prioritet
3. **Ramverks-chatten producerade tre dokument:**
   - Arbetsorder för implementering (`arbetsorder-design-omgang-1.md`)
   - Uppdaterad komponentdokumentation (`KOMPONENTER-INNEHALL.md v1.2`)
   - Denna veckogenomgångs-uppdatering till PLATTFORMS-ANDRINGAR.md
4. **Code utför inventeringar** innan ändringar (för fyra av fem punkter)
5. **Joachim verifierar visuellt** i Live Server efter implementation
6. **Båda repon uppdateras** parallellt eftersom CSS är delad

Genomförandetid: ~1-2 dagar elapsed time (mest väntetid mellan rapportering och godkännande).

---

## Lärdom för framtiden

Tre observationer från denna veckogenomgång värda att bära med:

1. **Eleverfeedback överträffar designintuition.** Tre konkreta elev-observationer ledde till klarare beslut än kollegans (rimliga men generella) designförslag.

2. **Inventera innan du ändrar.** Code:s mönster att rapportera nuvarande tillstånd innan ändring sker — etablerad efter fordj-kort-incidenten — fungerar utmärkt även för designjusteringar.

3. **Två omgångar är bättre än en stor.** Genom att skjuta Omgång 2 (sticky header, djupare designval) får vi mäta effekten av Omgång 1 innan vi bygger vidare. Mindre risk att ändringar krockar med varandra.
