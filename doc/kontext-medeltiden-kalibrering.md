# Kontext — Medeltiden-kalibrering

> Bilaga till `kontext-historiabok.md`. Specifik kalibrering för 
> Medeltids-kapitlet — stilistik, struktur, accentfärger, scope.

---

## SYFTE

Kontextdokumentet säger *vad* och *vem* generellt för Historia. Det här dokumentet säger *kalibrering* för Medeltiden specifikt — så det landar i samma rytm som Geografi-piloterna.

Läs båda dokumenten innan produktionen börjar.

---

## SCOPE — TRE DELKAPITEL

Joachim har skissat följande scope. **Avsnittsindelningen är inte slutgiltig** — den kan utvecklas under produktion (slå ihop teman, dela upp större ämnen, lägga till saknade).

### 1. Tidig medeltid
- a. Folkvandring
- b. Kyrkans betydelse och utveckling
- c. Den arabiska expansionen och Karl den Store
- d. Feodalism och ståndssamhälle

### 2. Högmedeltiden
- a. Jordbruksutveckling och kyrkans roll
- b. Stadsutveckling och universitet
- c. Handelsutveckling, penninghushållning och handelscentrum
- d. Korstågen

### 3. Senmedeltiden
- a. Digerdöden och böndernas situation (klimatets påverkan vävs in här)
- b. Maktkamp mellan kyrka och kung
- c. Kinas påverkan på Europa (Marco Polo, kunskap, varor)
- d. Renässansen (övergång till nästa epok)

**Notera:** Vissa avsnitt hänger ihop tematiskt — t.ex. Jordbruksutveckling (2a) leder till Städer (2b). Innehållsproducenten avgör om sådana avsnitt blir egna sidor eller får underdel-väljare (A/B inom samma avsnitt). Som med Geologi: pedagogiskt val per avsnitt.

---

## ACCENTFÄRGER — MANUSKRIPTSSTÄMNING

Medeltiden ärver Historia-bokens accentfärger från `css/historia.css`:

```css
--accent: #5a1a2a     /* djup vinröd */
--accent-2: #7a5a2e   /* mörkt brons */
```

Övriga tokens (paper, ink, brass, blood, terra) ärvs oförändrade.

**Inom Medeltids-kapitlet** kan enskilda delkapitel introducera **max 2 nya färger** som tematisk identitet inom vintageatlas-ramverket. Inte beslutat ännu — låt det växa fram. Exempel som *kan* motiveras:

- Senmedeltidens digerdöden-avsnitt: mörkare askgrå + sjuk grön
- Korstågsavsnittet: ökensand + djupare blod

Eller inga extra färger — accent och accent-2 räcker. Pedagogiskt val per delkapitel.

---

## REFERENS — LÄS INNAN DU BÖRJAR PRODUCERA

Två sidor i Geografi-piloterna visar etablerad ton, längd, struktur och pedagogisk rytm:

- `https://jb873.github.io/Geografibok/delkapitel/demografi/avsnitt-3-demografisk-transition.html`
- `https://jb873.github.io/Geografibok/delkapitel/geologi/avsnitt-3-jordbavningar.html`

Läs båda på alla tre nivåer (📗 📘 📕). Demografi är mer kausalt-resonerande (passar Medeltidens makro-skeenden). Geologi är mer process-orienterat (passar avsnitt om hur jordbruk eller stadsplanering förändras).

Den nya Medeltids-texten ska matcha rytmen — inte uppfinna något nytt.

---

## VOLYM PER AVSNITT — KALIBRERING

Demografi-pilotens och Geologi-kapitlets riktmärken:

- **Textnivåer:** 📗 ~250-400 ord, 📘 ~500-700 ord, 📕 ~800-1100 ord
- **1-2 bildguider + bilder** per avsnitt
- **1 kärnpunkter-block** per avsnitt (eller 2 om avsnittet täcker två parallella delar)
- **1-3 djupdykningar** länkas från varje avsnitt
- **~20-30 flipcards per avsnitt**, fördelat ungefär 50/30/20 mellan begrepp/tillämpning/resonemang

Detta är riktmärken, inte gränser. Korstågen kan rättfärdiga fler avsnitt; Renässans-övergången kan vara kortare.

---

## ETABLERAD VOKABULÄR (snabbreferens)

Termer som används utan förklaring i denna kontext och i dialog:

- **Packing-upp av kausala kedjor** — orsak-verkan-resonemang som prosa, inte bullet-listor
- **Advance organizer** — text som förbereder eleven på vad hen ska möta (bildguider innan bilder)
- **Sambandsled / konnektorer** — språkliga uttryck som binder ihop resonemang (»därför att«, »vilket ledde till«, »trots att«). Universellt bibliotek finns i `data/konnektorer.json`
- **Stödord och startfraser** — hjälpsystem på flipcards-redogörelsekort: begrepp eleven förväntas använda + meningsbörjar
- **Differentiering** — samma innehåll på tre nivåer

---

## AVGRÄNSNING MELLAN TEXT OCH DJUPDYKNING

I **huvudtexten:** det varje elev (på den nivån) behöver kunna.

I **djupdykning:** fördjupning, exempel, kuriosa, historiska sidospår, kontroverser i historieforskningen.

**Tumregel:** om innehållet inte testas eller refereras tillbaka till i flipcards eller redogörelsekort, hör det troligen hemma i en djupdykning — inte i löpande text.

### Specifikt för Historia
Historia har särskild risk att svälla med detaljer. Disciplin:
- **Namn på personer:** med i texten bara om eleven måste kunna namnet (Karl den Store, ja; Roland av Bretagne, nej)
- **Datum:** med i texten bara om årtalet är epokmärkande (1066, 1453, 1492). Generellt undvik åratal i löpande text — säg "i mitten av 1100-talet"
- **Geografiska detaljer:** generella regioner i texten, exakta orter i djupdykning

---

## BILDPALETT — MEDELTIDA TONER

Bas-prompten är samma som Geografi (vintageatlas-stil). Variera bara dominerande färgton för Medeltiden:

> Färgtonen lutar åt sepia, pergamenttoner, djup vinröd och brons. 
> Tänk medeltida manuskripts-illuminationer — varma jordtoner och guld-detaljer. 
> Behåll vintageatlas-baskaraktär (papper, bläck, etsnings-/atlas-känsla).  
> Undvik mossgrön och marinblå som dominerande toner.

**Inom Medeltiden ska bilderna hänga ihop** — alla avsnittsbilder bör kännas som en sammanhängande serie. Om Folkvandrings-bilden är sandtonad och Universitets-bilden är blå-vit-litografi ser kapitlet osammanhängande ut.

**Mellan kapitel ska skillnaden vara subtil.** Eleven ska känna Alphaskolan först, Medeltiden sen.

**Test:** när 5-6 testbilder är gjorda, lägg dem bredvid Geografi-bilder och fråga om relationen är *familjär men tydligt egen*. Om svaret är "samma" eller "helt olika" — kalibrera om.

---

## SÄRSKILDA UTMANINGAR FÖR MEDELTIDEN

### Risk att Medeltiden romantiseras eller demoniseras
Eleverna har förutfattade meningar om "den mörka medeltiden". Historia 7-9 ska visa både kontinuitet (Antikens arv lever vidare via kloster och muslimsk översättning) och förändring (städer, universitet, handel). Inte "myten om barbari" eller "myten om upplyst guldålder".

### Risk att eurocentrism dominerar
Den arabiska expansionen och Kinas påverkan är två avsnitt där icke-europeiska perspektiv är centrala. Skriv inte dem som "exotiska intermezzon" — de är delar av medeltidens världshistoria.

### Religion utan teologi
Eleverna ska förstå kyrkans roll som politisk, ekonomisk och kulturell aktör — inte som teologisk lärare. Diskussion om dogm och tro hör inte hemma i Historia 7-9. Däremot diskussion om makt, organisation, ekonomi och påverkan på samhället.

### Konkretiseringar i klassrumsspråk
Medeltiden är abstrakt för 13-åringar. Konkretisera:
- "En vanlig bonde åt nästan aldrig kött. Bröd och gröt, dag ut och dag in."
- "En stad på 5000 invånare var stor. Stockholm hade kanske 2000 medeltiden ut."
- "Att resa från Stockholm till Paris tog flera månader. Inte timmar."

Sådana konkretiseringar gör tidsperioder begripliga.

---

## VOLYM-PROGNOS FÖR MEDELTIDEN

Baserat på Joachims kommentar "färre begrepp och färre självskattningsmoment":

- 10-14 avsnitt (3 delkapitel × 3-5 avsnitt)
- ~40-50 begrepp totalt (3-4 per avsnitt)
- ~40-50 självskattningsmoment (begrepp grupperade + färdigheter)
- ~12-18 djupdykningar
- ~350-550 flipcards totalt

Vid första avsnittet — kalibrera. Om Folkvandrings-avsnittet rättfärdigar bara 15 flipcards (litet ämne), bra. Om det rättfärdigar 35 (tätt med begrepp), bra. Riktmärket är inte krav.

---

## FÖRSTA STEGET

Joachim har följande lista att producera:

1. **Tidig medeltid → Folkvandring** (första avsnittet, mest kalibrering)
2. När det landar i rätt rytm — fortsätt med Kyrkans betydelse och utveckling
3. Etc.

Säg "kalibrering förstådd, börjar med Folkvandring" när du läst detta så vet Joachim att vi är synkade.
