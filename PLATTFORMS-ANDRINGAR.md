# Plattforms-ändringar — Alphaskolans lärplattform

> Pedagogisk arbetsdagbok. Här samlas observationer som *kan* påverka 
> plattformen — innan de blir formella ändringar. Förhindrar drift 
> mellan böcker och kapitel.

**Starta varje arbetsdag med att kolla 🔵-listan.** 
**Veckogenomgång:** söndagar (eller när 🔵-listan har 3-5 poster).

---

## Snabbreferens — tre typer av ändringar

| Typ | Vad | Hantering |
|---|---|---|
| **A** Innehåll | Texten i ett avsnitt, en bild, en faktaformulering | Fixa direkt. Gå vidare. Hör inte hemma här. |
| **B** Mönster | Hur en komponent ser ut eller fungerar (flikar, kort, navigation) | Lägg i 🔵-listan nedan. Ändra INTE direkt i boken. |
| **C** Plattform | Pedagogisk modell (trösklar, lägen, korttyper, kunskapskrav-modell) | Lägg i 🔵-listan nedan. Ändra INTE direkt i boken. |

**Tumregel:** Om upptäckten kan tänkas påverka *ett annat avsnitt eller en annan bok* → det är B eller C. Skriv ner.

---

## Statuskoder

| Symbol | Betydelse |
|---|---|
| 🔵 | Ny observation — att bedöma på nästa veckogenomgång |
| 🟡 | Beslutat — väntar på implementation |
| 🟢 | Implementerat i plattformsspec — väntar migration av befintliga böcker |
| ✅ | Klart överallt |
| ⏸️ | Pausat / skjutet framåt |
| ❌ | Förkastat efter övervägande |

---

## 🔵 Aktiv lista — att bedöma

| Datum | Typ | Var upptäckt | Observation | Förslag |
|---|---|---|---|---|
| 2026-06-15 | C | Historiabok-omstart | 13 JS-moduler har `geo-` hårdkodat som localStorage-prefix; 6 moduler defaultar ämne till `geografi`. Ingen central konfigurationspunkt. | Gemensam `AMNE_PREFIX`-mekanism i plattformskomponenterna. Geografi `geo` (bakåtkompat), Historia `hist`. Berörda: elevbok, egna-fragor, avsnitt, avsnitt-elevbok, kapitel-elevbok, kapitel-begreppsbank, amne-elevbok, amne-begreppsbank, sjalvskattning-vy, elevdata-overforing, flipcards, sparning, elevbok-stodlarare (avaktiverad). |
| 2026-06-15 | C | Historiabok-omstart | Accentmodellen skiljer sig mellan böcker: i Geografi bor `--accent`/`--accent-2` i en kapitel-override (geologi.css), men Historia behöver dem på bok-nivå (historia.css) som bokidentitet. CLAUDE.md beskriver inte denna spegelvändning tydligt. | Förtydliga i plattformsspec/CLAUDE.md: bok-override (accenter) vs kapitel-override (max 2 extra färger). Historiabok har redan löst det via css/historia.css. |
| 2026-06-15 | C | Historiabok-omstart | `forelasningar.js` och `avsnitt-elevbok.js` har hårdkodade `fetch('data/…')`-sökvägar relativt sidan. Fungerar i Geografi (data/ är syskon, 2 nivåers nesting) men bryter när sidnesting blir djupare. Historia har 4 nivåers nesting (kapitel/medeltiden/delkapitel/tidig/avsnitt-…html), där data/ ligger två nivåer upp. `flipcards.js` är OK (sökväg via `data-fil`-attribut) men dess BILD_BAS `../../img/` har samma problem. | Generaliseras **tillsammans med AMNE_PREFIX-arbetet** (samma moduler berörs): konfigurerbar bas-sökväg eller relativ-till-rot, alternativt `data-`-attribut som flipcards. Berör alla böcker med >2 strukturnivåer. |
| 2026-06-16 | C | Historiabok, Folkvandring-integration | Innehållsproduktionens per-avsnitt-JSON (fragor/begreppsbank/matris) har en rikare/annan schema-form än plattformens nuvarande JS konsumerar. Ex: `elevbok-fragor-avsnitt-1.json` har `avsnitt` som sträng + `fragor` på toppnivå med `grupp`/`rubrik`/`stodtext`/`policy`, men `avsnitt-elevbok.js` förväntar `data.avsnitt` som array filtrerad på `id` + `typ`-fält. Begreppsbank (etymologi) och matris (skalor, policy) liknande. Arbetsordern la dessutom elevbok/matris-källor i undermappar (`data/elevbok/`, `data/matris/`) medan CLAUDE.md/JS använder platt `data/`. | Aligna i samma svep som AMNE_PREFIX + datasökväg: fastställ kanoniskt JSON-schema (uppdatera plattforms-JS att läsa de rikare per-avsnitt-filerna, ELLER definiera ett dokumenterat aggregations-/transformsteg) och kanonisk placering (platt `data/`). Tills dess hålls käll-JSON orörda; de flata skeletten (fragor/begreppsbank/matris.json) är tomma `{}`. |
| 2026-06-17 | Process | Ramverks-chatten, KOMPONENTER/LEVERANSGUIDE-INNEHALL | Ramverks-chatten dokumenterade fordj-kort-komponenten fel **två gånger** genom att läsa HTML-källan istället för att kontrollera mot CSS (faktisk rendering). | Komponentdokumentation ska verifieras mot faktisk rendering (CSS + webbläsare), inte bara HTML-källkod. Process-justering: ramverks-chatten ber Code verifiera CSS-stödet innan en komponent dokumenteras. |

*(Tom rad ovan är till för nya poster — fyll på underifrån)*

### Exempel på hur en post fylls i:

| Datum | Typ | Var upptäckt | Observation | Förslag |
|---|---|---|---|---|
| 2026-06-15 | C | Demografi-pilot, klassrum | 15 ord + nyckelord = för högt tröskel. Eleverna skrev korrekt men "fel" ord, blev blockerade. | 8 ord, inga nyckelord, dynamisk upplåsning |

---

## 🟡 Beslutat — väntar implementation

| Datum | Beslut | Påverkar | Status |
|---|---|---|---|
| 2026-06-15 | Begreppsbank: 15→8 ord, inga nyckelord, dynamisk upplåsning | Demografi-pilot, alla framtida ämnen | Arbetsorder skickad till Code |
| 2026-06-14 | Föreläsning blir egen flik bredvid Läs | Geologi, alla framtida avsnitt | Väntar tills Geologi-innehåll klart |
| 2026-06-14 | Historia byter till plattformens fonter (Marcellus SC + EB Garamond) | Historiabok Projekt 4 (50 filer) | Väntar tills Medeltiden är klar som ny mall |
| 2026-06-14 | Historia använder kapitel→delkapitel→avsnitt-terminologi | Hela Historiaboken | Migreras med Projekt 4 |

---

## 🟢 Implementerat i spec — väntar migration

| Datum | Ändring | Spec-version | Migration kvar |
|---|---|---|---|
| 2026-06-15 | Plattformsspec för elevbok/begreppsbank/självskattning/elevdata | Lager 2-3 v0.1 | Geografi: harmoniseras till `as-`-prefix vid BEM-migration |
| 2026-06-17 | **Typ C:** `kapitel-begreppsbank.js` defaultar till `data/begreppsbank-{kapitel}.json` (kapitel-id-suffix), men Historias samlade fil heter `data/begreppsbank.json` → tom begreppsbank. **Lokal fix:** `window.BEGREPP_URL = 'data/begreppsbank.json'` satt explicit i `kapitelbegreppsbank.html` (samma mönster som `MATRIS_URL`). | Lokal fix (ej i spec än) | **Plattformsförslag:** `kapitel-begreppsbank.js` bör defaulta till `data/begreppsbank.json`, alt. läsa URL från `delkapitel-lista.json`. Påverkar Religion, Samhällskunskap, NO och alla framtida böcker som inte följer Geografis arvegodsmönster (`{kapitel}`-suffix). |

---

## ⏸️ Pausat / skjutet framåt

| Datum | Vad | Anledning |
|---|---|---|
| 2026-06-10 | Elevbok-stödläraren | Eleverna skriver i frågerutorna, inte i sammanfattning. Återupptas om elevbehov dyker upp. |
| 2026-06-14 | Dark mode | Vintageatlas-paletten är hela designens kärna. Bryts av dark mode. |
| 2026-06-14 | AI-stöd i läromedlet | Tills kostnadseffektiv lösning finns. |

---

## ✅ Klart överallt (för historik)

| Datum | Ändring |
|---|---|
| 2026-06-14 | Geografibokens palett kodifierad som plattformens Lager 1 |
| 2026-06-14 | Marcellus SC + EB Garamond låsta på plattformsnivå |
| 2026-06-14 | Geografi-piloten klar (6 avsnitt × 3 nivåer, 145 flipcards, 11 djupdykningar) |

---

## ✅ Genomfört

| Datum | Typ | Ändring | Påverkar | Status |
|---|---|---|---|---|
| 2026-06-17 | B | Kapitelverktygs- och självskattningslayout kopierad från Geografi till Historia. Sidorna fick Geografis sid-chrome (`titelblock`, `ornament-rad`, `sektion-avgransare`/`resurser-rad`) och sidopanels-layout (`kelev-layout` + `kelev-nav` + `kelev-innehall`, `kelev-sokrad`, `kelev-stats`) samt korrekta mount-id:n. **Ingen CSS-ändring** (alla klasser fanns redan i `css/geografi.css`). **Ingen JS-ändring** (Historias kapitel-JS hade redan identiskt DOM-kontrakt med Geografi). Historia-innehåll bevarat: brödsmulor, medeltids-avsnitt, kapitel-prefixade filnamn, MATRIS_URL. **Accenter bevarade** via `css/historia.css` (`--accent: #5a1a2a`, `--accent-2: #7a5a2e`) — `geologi.css` länkas ej. Bonus: `kapitelelevbok.html` och `kapitelbegreppsbank.html` var felkopplade (`#…-host` mot JS som letar `#…-verktyg/-nav/-innehall`) och fungerar nu. | Historiabok/medeltiden (4 sidor). Mönster återanvändbart för alla ämnen med kapitel-verktygssidor. | ✅ Verifierat http: alla sidor + data + JS 200 |
| 2026-06-17 | C | fordj-kort-strukturen dokumenterad i `KOMPONENTER-INNEHALL.md` (ramverks-chatten). Inventering av djupdyknings-sektionen i Historias 8 avsnitt (tidig 1–4 + hög 5–8) bekräftade att alla redan har korrekt kanonisk inre struktur (`fordj-kort-ikon` + `fordj-kort-text` > `fordj-kort-titel`/`fordj-kort-sammanfattning`, inline-spans, riktiga emojis). Ingen `<h3>`/`<p>`-bugg kvar (avsnitt 7–8 fixade i tidigare arbetsorder). **Ingen filändring behövdes.** Rubriken behålls som `<span class="sektion-label">` — kanonisk struktur enligt KOMPONENTER-INNEHALL.md v1.1 för nya böcker. (Geografis `<h2>` renderas korrekt via CSS och är acceptabel legacy — verifierat visuellt på live-Geografi.) | Historiabok/medeltiden, avsnitt 1–8 | ✅ Inventerat, 0 filändringar |
| 2026-06-21 | B | Städning av `data/`-roten: tog bort **9 fritt liggande arkivkopior** av innehållssessionens per-avsnitts-leveranser (`begreppsbank-avsnitt-3/5/6/7/8.json` + `avsnitt-9/10/11/12-*.json`). Verifierat före radering: ingen JS-modul läser dem (grep `js/` = 0 träffar), och allt innehåll finns i samlade `begreppsbank.json` (76 begrepp). Samlade filer (`begreppsbank/fragor/matris/forelasningar.json`) + `flipcards/` oförändrade. Spårbarhet via git-historik. | Historiabok/data (Geografi redan ren) | 🟢 `git rm` + separat commit |
| 2026-06-21 | B | **Designjustering Omgång 1** (elev- + kollegafeedback), 5 ändringar i delade `css/geografi.css` (print-CSS orört). **A1:** brödtext 18→19px (`body` 1.125→1.1875rem + `.flik-innehall` 18→19px). **B1:** ny `--brass-text: #785b13` (WCAG AA 4.9:1 på paper) — alla `color: var(--brass)` (63 st) → `--brass-text`; dekorativ `--brass` (border/bg) behållen. Muted-audit: ingen primär lästext använder `--muted` (brödtext = `--ink`, AAA) → muted oförändrad. **B2:** `.sida` 900→1040px + brödtext-block `max-width: 64ch` (60–75 tecken/rad); bilder bryter ut bredare. **B3:** `.brodtext h3` 1.2rem + letter-spacing + `--ink`; `.brodtext h2` border-bottom i brass. **B4:** tunn border-top `rgba(27,42,54,0.10)` + luft före varje brödtext-h2 (utom första). | **Båda repon** (Historia + Geografi — identisk CSS) | 🟢 Implementerat; **väntar Joachims visuella verifiering** 1366×768 + print |
| 2026-06-21 | B | **Finjustering av Omgång 1 (B2):** `max-width: 64ch` på brödtext-blocken gjorde att `h2` (större font) blev ~222px bredare i pixlar än brödtexten (mätt: h2 992px vs brödtext ~770px) — `ch` är relativt varje elements egen font. Infört `--las-bredd: 770px` (= brödtextens nuvarande px-bredd) och bytt blockens `max-width: 64ch` → `var(--las-bredd)`. Nu linjerar alla brödtext-block (p/h2/h3/h4/ul/ol/blockquote/aside/karnpunkt/bildguide) oavsett font; brödtexten står still, h2 krymper till samma kant. `.brodtext-bild` orörd. | Båda repon | 🟢 Implementerat; väntar visuell verifiering |
| 2026-06-21 | B | **Föreläsnings-flik `disabled` vid tom data.** `forelasningar.js` sätter nu `disabled` + `aria-disabled="true"` på `.flik[data-flik="forelasning"]` när avsnittet saknar föreläsningar (samt i catch vid 404/fetch-fel). Ny CSS `.flik[disabled], .flik[aria-disabled="true"]` (opacity 0.4, `cursor: not-allowed`, `pointer-events: none`) i delade `geografi.css`. **Obs:** `forelasningar.js` var **inte** identisk mellan repon (Historia har `dataBas()`-patch för djupare nesting, Geografi hämtar `data/` direkt) → samma disabled-logik infördes i båda **separat**, varje fil behåller sin fetch-sökväg. Påverkade avsnitt: Medeltiden a1/a2/a3/a4/a7/a10 disablas; Geologi/Demografi enligt respektive `forelasningar.json`. | Båda repon (delad CSS; JS-logik speglad) | 🟢 Implementerat; väntar visuell verifiering |
| 2026-06-21 | B (ny komponent) | **Sticky tidslinje-header (Historia-del).** Ny `.tidslinje-header` (sticky, top:0, accent-gradient) + `js/tidslinje.js` (läser `data-fil` → avsnittslista.json, markerar `AVSNITT_ID` som "Du är här", `aria-current`). Ny datafil-typ `avsnittslista-{delkapitel}.json`. Spec: spec-sticky-header.md. **Beslut från inventeringen:** (1) default `--accent: #1e5c7a` / `--accent-2: #b8902a` lagt i `geografi.css :root` (Geografi får ocean-blå; Historia överskrivs av `historia.css`, vinröd bevaras). (2) label-färg `rgba(232,222,200,.7)` istället för `--brass-text` (annars mörkt-på-mörkt). (3) Placering: efter `<body>`, **före** `.sida` (full bredd). Implementerat i Historia: 12 avsnitt + 3 avsnittslista-filer + scaffold-mall. **Kvar:** Geografi (avsnittslista + sidor) väntar på beslut om årtals-format; 76 djupdyknings-headrar (separat arbetsorder); hög/sen-årtal är approximativa (flaggade för granskning). | Delad CSS+JS i båda; Historia-sidor wire:ade | 🟡 Historia klart lokalt; Geografi + djupdykning kvar; väntar visuell verifiering |
| 2026-06-22 | B (mönster) | **Mörk hero-banner per avsnitt (Historia).** Ny `.hero-banner` (gradient `#1a0e08→#2a1810`, ~150px, centrerad) som **ersätter** `.avsnitt-header` + den fristående brödsmulraden — brödsmulorna flyttade in i bannern (med `aria-label`/`aria-hidden`/`aria-current`), plus label + titel (Marcellus SC, clamp 30-42px) + subtitel. Placeras mellan tidslinje-headern och `.sida`. Den gamla dekorativa accent-staven städades bort (blev föräldralös). Print döljer bannern. Arbetsorder: arbetsorder-mork-hero-banner.md. 12 avsnitt scriptade (varje sidas egna brödsmulor/label/titel/subtitel bevarade) + scaffold-mall uppdaterad. CSS delad till Geografi men **vilande** (inga `.hero-banner`-element där). | Historia-sidor; delad CSS i båda (Geografi oberörd) | 🟡 Implementerat lokalt; väntar visuell verifiering |
| 2026-06-22 | B (ny funktion) | **Elevfeedback-knapp (mailto).** Ny `js/elevfeedback.js` + CSS: floating "💬 TIPSA" bottom-right på **alla** sidtyper (knapp + modal med kategori/kommentar → bygger `mailto:`-länk till `jb@alphaskolan.se` med sidtitel/URL/tid). Injicerat i **64 Historia + 65 Geografi-sidor** (djupberoende sökväg) + scaffold-mall. **Beslut från inventeringen:** spec:ens z-index (knapp 1000 / overlay 1001) krockade med befintliga modaler (export-modal 1000, bild-lightbox 1100) → satte knapp **990** (göms under modaler) + overlay **1300** (över alla). Esc + klick-utanför + tom-kommentar-varning tillagt. Print döljer knapp+overlay. Arbetsorder: arbetsorder-elevfeedback-knapp.md. | Båda repon (delad CSS+JS + skript på alla sidor) | 🟡 Implementerat lokalt; väntar visuell verifiering. Geografi pushas efter OK. |
| 2026-06-22 | B (finjustering) | **Hero-banner: tightare övergång till innehåll.** Glipan banner→flikrad var ~104px (`.sida` padding-top 4.5rem + `.flikar-rad` margin-top 2rem). Ny regel `.hero-banner + .sida { padding-top: 0.5rem }` → ~40px, gäller **bara** avsnittssidor (adjacent sibling) så global `.sida`-padding (sidor utan banner) är orörd. Accent-staven förblir borttagen (bekräftat av Joachim — mörk banner räcker som separator). | Båda repon (delad CSS) | 🟢 Implementerat lokalt; väntar visuell verifiering |
| 2026-06-22 | B (rättning) | **Elevfeedback: `mailto:` → Gmail-compose-URL.** Joachims test kom inte fram — `mailto:` skickar aldrig automatiskt, bara öppnar ett utkast i enhetens standard-mailhanterare, vilket inte är konfigurerat på Chromebooks (Gmail-skola). Bytte i `elevfeedback.js` till `https://mail.google.com/mail/?view=cm&fs=1&to=…&su=…&body=…` som öppnas i ny flik (`window.open`) — Gmails skrivruta direkt i webbläsaren för inloggade elever, ingen mailhanterare krävs. Eleven klickar fortfarande "Skicka" (helautomatik kräver backend, uteslutet i ordern). | Båda repon (delad JS) | 🟡 Implementerat lokalt; väntar Joachims test |
| 2026-06-22 | B (komplettering) | **Djupdyknings-headers (76 sidor).** Sticky tillbaka-header `<header class="tidslinje-header djupdykning">` med `← Tillbaka till {avsnitt}` på alla 76 djupdykningar (41 Historia + 35 Geografi). Återanvänder befintlig CSS från sticky-header-jobbet. **Mappning självdeklarerad:** varje sidas egen `.tillbaka-lank` gav href+text (73 sidor; underdel-hash bevarad → bonus B2 gratis). 3 Geologi-djupdykningar (kolahalvon, polarsken, polskiften) saknade `.tillbaka-lank` men hade brödsmulor+`fordj-kort` → mappade manuellt. Botten-länken behållen (B3 alt a). 0 brutna länkar (alla 76 mål verifierade). Arbetsorder: arbetsorder-djupdyknings-headers.md. | Båda repon (HTML; CSS fanns redan) | 🟡 Implementerat lokalt; väntar visuell verifiering |
| 2026-06-22 | B (design) | **Mörk hero-banner på djupdykningar (basversion).** Tidigare parkerat (fråga 6b). Djupdykningarnas ljusa `.avsnitt-header` (label + titel + underrubrik + brödsmulor) wrappad in i den mörka `.hero-banner` (återanvänd från avsnitten) — sticky tillbaka-baren kvar ovanför. Variant-tålig omvandling över 76 sidor: 62 standard (brödsmulor+header), 11 demografi (utan brödsmulor), 3 special-geologi (`avsnitt-header djupdykning-header`, emoji-label, `<main class="sida">`). Inga extras (ornament/tvåfärgad titel/SKRIV UT — medvetet utelämnat). **Trade-off:** djupdyknings-titeln ligger nu i den print-dolda `.hero-banner` (förut i `.avsnitt-header` som syntes i print) → titeln försvinner vid utskrift av en djupdykning. Flaggat. | Båda repon (HTML; CSS fanns) | 🟡 Implementerat lokalt; väntar visuell verifiering |
| 2026-06-21 | A (innehåll) | **Nytt kapitel: Upptäckternas tidevarv — avsnitt 1 Bakgrund.** Kapitel-scaffold speglar medeltiden (`kapitel/upptackterna/`: index + `delkapitel/upptackterna/` + `data/`). Avsnitt 1: 4 underdelar A–D × 3 nivåer (12 texter, md→HTML via byggscript), bild på Enkel+Standard (ingen på Fördjupning), figcaption = arbetsorderns kärnbudskap. 3 djupdykningar (Vespucci, Magellan/Elcano, Upptäckare efter Columbus) med tidslinje-tillbaka + hero-banner + tillbaka-länk `#d`. `avsnittslista-upptackterna.json` för tidslinjen. Historia-startsidans kort IV aktiverat. **Avvikelser mot ordern:** BEM/`as-`-namn används ej (repot är flat naming); §A-bild = `handeln-med-asien-blev-dyrare.webp`. **Provisoriskt/flaggat:** bildguide-text (platshållare, content fyller), avsnitts-/delkapitel-/kapitel-underrubriker, bild-alt, årtal `~1450-1500`, alla djupdyknings-anchors `#d` (Vespucci ev. `#c`). Pending (ej i denna leverans): datafiler (frågor/begrepp/matris/föreläsning) + Öva. | Endast Historia | 🟡 Byggt lokalt; väntar visuell verifiering + content-komplettering |
| 2026-06-21 | A (innehåll) | **Upptäckterna Bakgrund — Enkel-bildguider inlagda + Vespucci-anchor.** Content re-levererade Enkel-nivåerna (zip) med riktig `### 👁 Bildguide` (ingress "Titta på kartan innan du läser vidare:" + 4–5 punkter). Bytte platshållarna mot riktig bildguide i alla 4 underdelar (`.bildguide` + `.bildguide-rubrik "👁 Bildguide"` + `<p>`-ingress + `<ul>`) och regenererade Enkel-prosan från de nya filerna. Vespucci-djupdykningens tillbaka-länk ändrad `#d`→`#c` (Columbus) per arbetsorderns testchecklista; Magellan + Upptäckare efter Columbus kvar på `#d`. | Endast Historia | 🟡 Implementerat lokalt; väntar visuell verifiering |
| 2026-07-02 | A (innehåll) | **Upptäckterna avsnitt 2 Orsaker.** 4 underdelar §B1–B4 (Teknik/Ekonomi/Nya idéer/Religion) × 3 nivåer (md→HTML via byggscript), Enkel med inbakad bildguide, **inga djupdykningar** (inga fordj-kort). §B1 Fördjupning har egen bild `karavellen-teknisk-detalj.webp` (undantag, ingen bildguide); sammanfattande **konceptbild** `fyra-orsaker-till-uppttackterna.webp` efter §B4 i Läs-panelen. Föreläsning = disabled-platshållare. `avsnittslista-upptackterna.json` + delkapitel-index uppdaterade (Orsaker aktiv, Konsekvenser dimmad). **⚠️ 6 bildfiler saknas** (endast promptar levererade) → img-referenser 404:ar tills de läggs i `img/`: `teknik-som-gjorde-uppttackterna-mojliga`, `karavellen-teknisk-detalj`, `varfor-europa-ville-ut`, `renassansens-verkstad`, `reconquista-och-1492`, `fyra-orsaker-till-uppttackterna` (obs stavning "uppttackterna" enligt ordern). Provisoriskt: underrubrik, bild-alt, årtal `~1400-1500`. | Endast Historia | 🟡 Byggt lokalt; väntar bildfiler + visuell verifiering |
| 2026-07-02 | A (innehåll) | **Upptäckterna avsnitt 3 Konsekvenser — delkapitlet komplett.** 4 underdelar §A–D (Möte med Amerika/Triangelhandeln/Slavhandeln/Columbianska utbytet) × 3 nivåer (Enkel med inbakad bildguide), konceptbild `fyra-konsekvenser-formar-varlden.webp` efter §D. **3 djupdykningar** (Tenochtitlán `#a`, Slavupproren `#c`, Slavhandeln i Afrika `#c`) — nu **med egna bilder** (figur överst i artikeln, `bildmodal.js` inlagd för klick-förstoring). 8 nya bilder committade (alla på plats i `img/`). Föreläsning = disabled-platshållare. `avsnittslista-upptackterna.json` + delkapitel-index uppdaterade → **alla 3 avsnitt aktiva**; Upptäckterna-delkapitlet klart (utom datafiler + Öva). Provisoriskt: underrubriker, bild-alt, årtal `~1500-1800`. | Endast Historia | 🟡 Byggt lokalt; väntar visuell verifiering |
| 2026-07-03 | A (innehåll) | **Upptäckterna: datalager.** `fragor.json` (17 frågor → Elevbok-fliken), `begreppsbank.json` (21 begrepp, mergad från 3 avsnittsfiler, `kallfil`-path fixad), `flipcards/avsnitt-{1,2,3}.json` (→ Öva-fliken). **Personkort-lösning (Joachims val):** de 20 personkorten flyttade in i `begreppskort` med `type:"begrepp"` så de renderar i Begrepp-läget som vanliga kort — **ingen ändring i delade `flipcards.js`** (Geografi orörd). Alla 47 kort renderar (41 begrepp+person i niva1, 6 redogörelse i niva3). Obs: niva2 "Tillämpning" (modellkort) är tomt för Upptäckterna (inga modellkort levererade) — hanteras grafiskt. **Kvar:** `kapitelbegreppsbank.html`-sida för att visa de 21 begreppen; matris/självskattning + föreläsningar (separata leveranser). | Endast Historia | 🟡 Data på plats; begreppsbank-sida + matris kvar |
| 2026-07-03 | A (innehåll) | **Upptäckterna: kapitelverktyg (begreppsbank + elevbok).** Speglat medeltiden: `kapitel/upptackterna/kapitelbegreppsbank.html` (`window.BEGREPP_URL='data/begreppsbank.json'`, visar de 21 begreppen med Modell A + sök + avsnittsfilter) + `kapitelelevbok.html` (laddar `data/fragor.json`, samlade elevbokssvar). "Kapitlets verktyg"-sektion tillagd på kapitel-indexet med länkar till båda. Placerade på kapitel-nivå eftersom `kapitel-elevbok.js` hårdkodar `fetch('data/fragor.json')`. Självskattning utelämnad (matris ej levererad). | Endast Historia | 🟡 Byggt lokalt; väntar visuell verifiering |
| 2026-07-03 | A (innehåll) | **Reformationen (nytt delkapitel) — avsnitt 1 Reformationens uppkomst.** Andra delkapitlet i Upptäckternas tidevarv startat. 4 underdelar §1A–D (Kyrkans kris/avlatshandeln, Luther & 95 teserna, Brytningen med Rom, Bondeupproret) × 3 nivåer (Enkel med inbakad bildguide), konceptbild `reformationens-gnista-kedjereaktion.webp` efter §1D. 2 djupdykningar (Martin Luther `#b`, Tryckpressen `#c`) med egna bilder + bildmodal. 7 bilder i delkapitlets `img/`. Föreläsning = disabled-platshållare. Nytt `delkapitel/reformationen/index.html` + `avsnittslista-reformationen.json` (tidslinje); Reformationen-kortet aktiverat i kapitel-indexet. Provisoriskt: underrubriker, bild-alt, årtal `~1500-1525`. Pending: avsnitt 2–3 + datafiler + föreläsningar. | Endast Historia | 🟡 Byggt lokalt; väntar visuell verifiering |
| 2026-07-03 | B (mönster) | **Kapitelverktyg: 2-nivå-gruppering (delkapitel → avsnitt).** `kapitel-elevbok.js` + `kapitel-begreppsbank.js` grupperar nu per delkapitel när datat bär `delkapitel_titel` — delkapitel-rubrik "1. Upptäckterna" med avsnitt "a) Bakgrund / b) Orsaker / c) Konsekvenser". **Bakåtkompatibelt:** data utan `delkapitel_titel` (medeltiden/Geografi) renderar **platt som förut** (verifierat). Upptäckternas `fragor.json` + `begreppsbank.json` taggade med `delkapitel_titel`; tool-titlar → "Upptäckternas tidevarv". Ny CSS `.kelev-delkapitel-rubrik`/`.kelev-nav-grupp`/`.kelev-nav-sub`. **Endast delkapitel med data visas** (Joachims val) — Reformationen/Enväldet dyker upp automatiskt när deras data kommer. | Båda repon (delad JS+CSS; data endast Historia) | 🟡 Implementerat lokalt; väntar visuell verifiering |
| 2026-07-03 | B (design) | **Mörk hero-banner på ALLA nivåer (översiktssidor).** Tidigare bara på avsnitt/djupdykningar; nu även root-, kapitel-, delkapitel-index + kapitelverktygssidor (13 Historia-sidor). Samma `.hero-banner` — brödsmulor + label + titel (+ subtitel) flyttade in i mörk banner ovanför `.sida`; korten kvar ljust nedanför. Variant-tåligt (root utan brödsmulor; kapitel/tool med `.titelblock`; delkapitel med `.sektion-label`). Root: pattern-proof-accentstaven borttagen. **Endast Historia** — Geografis motsvarande sidor väntar på OK. | Endast Historia (CSS fanns) | 🟡 Implementerat lokalt; väntar visuell verifiering |

**Fil-mappning (Geografi → Historia) — för spårbarhet om samma sak dyker upp i annat ämne:**

| Geografi `delkapitel/{namn}/` | Historia `kapitel/{kapitel}/` | Mount-id:n (JS-kontrakt) |
|---|---|---|
| `index.html` | `index.html` | — (statisk; `resurser-rad` med 3 `resurs-kort`) |
| `elevbok.html` | `kapitelelevbok.html` | `kapitel-elevbok-verktyg/-nav/-innehall` |
| `begreppsbank.html` | `kapitelbegreppsbank.html` | `kapitel-begreppsbank-verktyg/-sok/-nav/-innehall` |
| `sjalvskattning.html` | `sjalvskattning.html` | `sjalvskattning-verktyg/-statistik/-nav/-innehall` |

> **Obs (kvarstående, ej layout):** Historias kapitel (`medeltiden`) spänner flera delkapitel (tidig/hög), medan Geografis modell antar ett delkapitel = en lagrings-namespace. `kapitelelevbok.html` sätter `DELKAPITEL_ID='medeltiden'` → elevsvar skrivna här synkar inte med per-avsnitt-svar (`geo-elev-svar-tidig`/`-hog`). Funktionell hierarki-fråga för ramverks-chatten, separat från denna layout-ändring.

---

## ❌ Förkastat

| Datum | Förslag | Anledning |
|---|---|---|
| | | |

---

## Veckogenomgång — söndag (eller när 🔵-listan har 3-5 poster)

**Tid:** ~30 minuter

**Steg:**

1. **Gå igenom 🔵-listan post för post.**
   - För varje: är det A (fel kategori — flytta ut)? B eller C (rätt)?
   - Bedöm pedagogiskt: är det rätt riktning?
   - Bedöm omfattning: är det en isolerad ändring eller pekar det på något större?

2. **Tre möjliga utfall per post:**
   - 🟡 **Godkänd** → flytta till 🟡-listan + skapa arbetsorder till ramverks-chatten
   - ❌ **Förkastad** → flytta till ❌-listan med kort motivering
   - 🔵 **Behöver mer underlag** → behåll i 🔵, anteckna vad som behöver utforskas först

3. **Granska 🟡-listan:**
   - Vilka kan släppas till implementation den här veckan?
   - Vilka väntar på något (t.ex. annan komponent klar)?
   - Finns det blockeringar att hantera?

4. **Granska 🟢-listan:**
   - Vilka migrationer ska göras den här veckan?
   - Behövs prioritering om kö växer?

5. **Reflektera över mönster:**
   - Dyker liknande observationer upp upprepade gånger?
   - Då pekar de mot något större — kanske en arkitektur-ändring snarare än enskild komponent.

**När det är klart:** stäng filen, fortsätt arbeta tryggt vetande att inget glöms.

---

## Regler

**1. Ändra aldrig direkt i en bok när du upptäcker B eller C.**
Lägg i 🔵-listan. Geologi-kapitlet får ha sin ofullständighet en dag till.

**2. Innehållsproduktion-chatten lägger till i 🔵.**
Den ändrar aldrig plattformen själv.

**3. Ramverks-chatten är den som flyttar mellan listor.**
Veckogenomgång görs där.

**4. Code-chatten implementerar 🟡 och 🟢.**
Den uppdaterar inte den här filen — det gör ramverks-chatten efter Code rapporterat klart.

**5. När i tvivel — skriv ner.**
Hellre en post för mycket än en ändring som glöms.
