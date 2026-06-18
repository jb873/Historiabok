# Komponenter — HTML-strukturer för innehållsproducenter

> Kanonisk dokumentation av återanvändbara HTML-komponenter i Alphaskolans 
> lärplattform. Bilaga till `LEVERANSGUIDE-INNEHALL.md`.
>
> Innehållssessioner ser inte CSS — bara HTML. För att producera 
> fungerande markup måste de exakta klassnamnen vara dokumenterade.

**Senast uppdaterad:** 2026-06-17 (v1.1)
**Version:** 1.1
**Källa för alla mallar:** Geografibokens Geologi-kapitel — verifierat **mot både HTML och CSS**

---

## Princip

Plattformskomponenter har **exakta klassnamn och struktur** som CSS:n kräver. Innehållsproducenten:

- Kopierar mallen rakt av
- Byter bara innehållet (text, länkar, ikoner)
- Ändrar INTE klassnamn, element-typer eller nesting-struktur

Vid tveksamhet — kolla Geografi-referensimplementationen.

### Dokumentationsprincip

Komponentstrukturer dokumenteras enligt **vad CSS:n faktiskt stilsätter**, inte enligt vad som råkar finnas i HTML-källkod. CSS är det som renderas för eleven. HTML kan ha legacy-element eller interna motsägelser.

---

## 1. fordj-kort (djupdykningskort)

### Pedagogisk funktion

Klickbara kort längst ner på en avsnittssida (i Läs-fliken). Pekar mot djupdyknings-HTML-filer. Synliga oavsett vilken underdel eller textnivå eleven har valt. Frivillig fördjupning.

### HTML-mall (kanonisk)

```html
<section class="djupdykningar">
  <span class="sektion-label">Vill du veta mer?</span>
  <div class="fordj-kort-grid">

    <a class="fordj-kort" href="djupdykning-{slug}.html">
      <span class="fordj-kort-ikon" aria-hidden="true">🌾</span>
      <span class="fordj-kort-text">
        <span class="fordj-kort-titel">{Titel på djupdykningen}</span>
        <span class="fordj-kort-sammanfattning">{1-3 meningar som lockar — vad eleven får ut av att läsa.}</span>
      </span>
    </a>

    <!-- Fler kort enligt samma mönster -->

  </div>
</section>
```

### Regler

- Rubriken är **`<span class="sektion-label">`** — inte `<h2>` eller annan rubrik
- `<div>`-griden heter **`fordj-kort-grid`** — inte `kort-grid`
- Allt textinnehåll inuti `<a>` är **inline `<span>`-element** — inga `<h3>`, `<p>` eller andra block-element
- `aria-hidden="true"` på ikon-spannet (skärmläsare läser inte emojin)
- Ikonen är en emoji som passar djupdykningens tema (🌾 jordbruk, 🕯 historiskt, 🌊 vatten, 🏔 berg, etc.)
- Sektionen har **ingen `id`**

### Varför `<span class="sektion-label">` istället för `<h2>`

CSS-regeln `.djupdykningar .sektion-label` stilsätter en brass-färgad, liten etikett som passar visuellt med vintageatlas-paletten. CSS:n har ingen regel för `.djupdykningar h2` — en sådan rubrik skulle rendera ostylad och bryta layouten.

**Notering:** Geografi-källans HTML innehåller faktiskt `<h2>` istället för `<span class="sektion-label">` i några avsnitt — det är en intern motsägelse mellan HTML och CSS som ska rättas i Geografi vid lämpligt tillfälle (loggad i PLATTFORMS-ANDRINGAR.md). Den kanoniska strukturen är vad CSS:n stödjer.

### Vanliga fallgropar

❌ **Fel:** `<h2>` som rubrik
```html
<section class="djupdykningar">
  <h2>Vill du veta mer?</h2>
  <div class="fordj-kort-grid">
```
Detta renderar en ostylad generisk h2-rubrik istället för den avsedda brass-etiketten.

❌ **Fel:** Block-element inuti `<a>`
```html
<a class="fordj-kort" href="...">
  <h3>Titel</h3>
  <p>Sammanfattning</p>
</a>
```
Detta renderas trasigt — kort blir horisontellt utflytna.

✅ **Rätt:** Span-etikett + inline-spans inuti kort
```html
<section class="djupdykningar">
  <span class="sektion-label">Vill du veta mer?</span>
  <div class="fordj-kort-grid">
    <a class="fordj-kort" href="...">
      <span class="fordj-kort-ikon" aria-hidden="true">🌾</span>
      <span class="fordj-kort-text">
        <span class="fordj-kort-titel">Titel</span>
        <span class="fordj-kort-sammanfattning">Sammanfattning</span>
      </span>
    </a>
  </div>
</section>
```

### Antal per avsnitt

Riktmärke: 1-3 djupdykningskort per avsnitt. Inte fler.

---

## 2. brodtext-bild (bilder med bildtext)

### Pedagogisk funktion

Bilder placeras **inom** brödtexten, inte efter den. Bildtexten förklarar varför bilden är där — vad eleven ska titta efter. `alt`-texten beskriver bilden för skärmläsare och tjänar också som teknisk dokumentation.

### HTML-mall (kanonisk)

```html
<figure class="brodtext-bild standard">
  <img src="../../img/{tema}/{bild}.webp" 
       alt="{Lång beskrivning av bilden — vad som syns, var saker är, hur de förhåller sig till varandra}">
  <figcaption>{Förklarande bildtext — vad ska eleven se?}</figcaption>
</figure>
```

### Per textnivå

`<figure>`-elementet har en nivå-klass: `standard`, `enkel` eller `fordjupning`. Samma bild kan ha olika `alt`-text och `figcaption` per nivå:

```html
<!-- I Standard-nivå-blocket -->
<figure class="brodtext-bild standard">
  <img src="../../img/{tema}/{bild}.webp" alt="{Detaljerad beskrivning}">
  <figcaption>{Standard-nivåns bildtext}</figcaption>
</figure>

<!-- I Enkel-nivå-blocket -->
<figure class="brodtext-bild enkel">
  <img src="../../img/{tema}/{bild}.webp" alt="{Kortare beskrivning}">
  <figcaption>{Enklare bildtext}</figcaption>
</figure>
```

### Regler

- Använd **`<figure>` + `<img>` + `<figcaption>`** — inte `<div>`-baserade konstruktioner
- `alt`-texten ska vara **utförlig och pedagogisk** (5-15+ ord) — inte bara "bild av X"
- `figcaption` förklarar **varför bilden är där** — inte vad den föreställer (det är `alt`-texten)
- Klassen `standard|enkel|fordjupning` matchar nivå-blocket bilden ligger i

### Filsökväg

Från avsnitts-HTML på 4-nivåers nesting (Historia): `../../img/{tema}/{bild}.webp`
Från avsnitts-HTML på 2-nivåers nesting (Geografi): `../../img/{tema}/{bild}.webp`

Sökvägen är samma eftersom `img/`-mappen ligger på samma nivå som `delkapitel/` i båda fall.

---

## 3. karnpunkter (Det viktigaste-block)

### Pedagogisk funktion

Sammanfattar 3-5 kärnpunkter från ett avsnitt — visuellt urskilt så eleven kan scanna eller revidera. Använder en "🎯 Det viktigaste"-rubrik som signal.

### HTML-mall (kanonisk)

```html
<div class="karnpunkter">
  <div class="karnpunkter-rubrik">🎯 Det viktigaste</div>
  <ul>
    <li>{Punkt 1 — kort, viktiga ord kan vara <strong>fetstilta</strong>}</li>
    <li>{Punkt 2}</li>
    <li>{Punkt 3}</li>
    <li>{Punkt 4 — max 5-6 punkter}</li>
  </ul>
</div>
```

### Regler

- `<div class="karnpunkter">` (inte `<aside>`)
- Inre rubrik är `<div class="karnpunkter-rubrik">`, **inte `<h3>`** — kärnpunkter-blocket är inte ett eget kapitel
- Rubriktexten innehåller alltid 🎯-emojin
- Punkterna är **kort prosa**, inte hela meningar med konnektorer ("därför att", "vilket ledde till"). Sådan kausalitet hör i löpande text.
- Fetstil för viktiga begrepp inom punkter

### Var i texten

`karnpunkter`-blocket placeras **innan eller efter en H2-rubrik** — antingen som introduktion till ett avsnitt eller som sammanfattning. Vanligast: nära slutet av en sektion, som "det här ska du komma ihåg".

### Antal per nivå

Riktmärke: 1-3 `karnpunkter`-block per textnivå per avsnitt. Inte fler.

---

## 4. bildguide (advance organizer för bild)

### Pedagogisk funktion

Förbereder eleven på vad hen ska titta efter i en specifik bild. Placeras **FÖRE** bilden (advance organizer-princip). Använder en "👁 Titta på bilden"-rubrik som signal.

### HTML-mall (kanonisk)

```html
<div class="bildguide">
  <div class="bildguide-rubrik">👁 Titta på bilden – {Kort beskrivning av vad bilden visar}</div>
  <p>{En inledande mening som sätter scenen}. Lägg märke till:</p>
  <ul>
    <li>{Punkt 1 — vad ska eleven specifikt titta efter}</li>
    <li>{Punkt 2}</li>
    <li>{Punkt 3 — max 3-5 punkter}</li>
  </ul>
  <p class="bildguide-fundera">Fundera: {En öppen fråga som kopplar bilden till elevens egen tanke}</p>
</div>
```

### Regler

- `<div class="bildguide">` 
- Inre rubrik är `<div class="bildguide-rubrik">` med 👁-emoji
- Inledande `<p>` slutar med "Lägg märke till:" eller motsvarande för att introducera punktlistan
- Punktlistan är **specifika observationer** — inte fakta från texten
- Avslutande `<p class="bildguide-fundera">` är **valfri** men rekommenderad — kopplar bilden till elevens egen reflektion
- Fundera-frågan ska vara öppen, inte ja/nej

### Placering

`bildguide` placeras **omedelbart före** `<figure class="brodtext-bild">` — så eleven läser guidens punkter och sedan ser bilden med rätt blick.

---

## 5. Komponenter som inte är dokumenterade ännu

Dessa kommer dokumenteras när konkret behov uppstår eller felmönster observeras:

- `flikar-rad` + `flik` (flikraden på avsnittssidor)
- `niva-valjare` + `niva-knapp` (📗📘📕-väljare)
- `underdel-valjare` + `underdel-knapp` (A/B/C/D-väljare)
- `kapitel-kort` (kapitelöversikt på startsidor)
- `resurs-kort` (kapitelverktygs-rad)
- `brodsmulor` + `skiljare` + `aktuell` (navigationsbrödsmulor)
- Kapitelverktygs-sidor (`kapitelelevbok.html`, `kapitelbegreppsbank.html`, `kapitelsjalvskattning.html`) — kommer dokumenteras efter pågående layout-fix är klar

Vid första felmönster i någon av dessa: **logga som Typ C-ändring** i `PLATTFORMS-ANDRINGAR.md`, så dokumenteras komponenten här.

---

## Process — när en ny komponent behöver dokumenteras

### Princip

Dokumentation av en komponent triggas av **ett verkligt felmönster** — inte av profylaktisk dokumentationsiver. För omfattande dokumentation som ingen läser är värre än ingen dokumentation alls.

### Verifieringskrav

Innan en komponent dokumenteras i denna fil **måste minst tre källor stämma**:

1. **HTML från Geografi-referensimplementationen** (vad som faktiskt produceras)
2. **CSS-regler i `css/geografi.css`** (vad som faktiskt stilsätts)
3. **Renderad visuell verifiering** (att rendering matchar avsikten)

Om HTML och CSS är internt motstridiga: **CSS vinner**. HTML-kvarlevor som inte stilsätts loggas som plattformsobservation för senare rättning.

### Steg

1. **Innehållssession** stöter på en komponent som inte är dokumenterad här
2. Sessionen **frågar Joachim** istället för att gissa
3. Joachim ger HTML-fragment från Geografi-referensimplementationen
4. **Ramverks-chatten verifierar mot CSS** innan dokumentation skrivs
5. Innehållssessionen levererar enligt facit
6. **Efter leverans:** Joachim ber ramverks-chatten lägga till komponenten i denna fil

Alternativ: Code stöter på trasig markup i en leverans och inte vet vad som är rätt. Samma flöde — frågar Joachim, eskalerar till ramverks-chatten för dokumentation, ramverks-chatten verifierar mot CSS innan svar.

### Vad varje komponentdel ska innehålla

För konsistens — varje komponent dokumenteras med:

1. **Pedagogisk funktion** — varför finns den, vad gör den för eleven
2. **HTML-mall (kanonisk)** — exakt struktur, kopierbar
3. **Regler** — vad som är låst, vanliga fallgropar
4. **Placering eller var i sidan** — om relevant
5. **Antal/riktmärken** — om relevant

---

## Bilagor — referensimplementationer

Källfiler i Geografi-repot där dessa komponenter syns (notera: HTML kan ha legacy-strukturer; CSS är den slutgiltiga referensen):

- **fordj-kort:** `delkapitel/geologi/avsnitt-3-jordbavningar.html` — OBS: använder `<h2>` istället för `<span class="sektion-label">`, en intern motsägelse. CSS:n stödjer `.sektion-label`.
- **brodtext-bild:** `delkapitel/geologi/avsnitt-3-jordbavningar.html` (flera instanser)
- **karnpunkter:** `delkapitel/geologi/avsnitt-3-jordbavningar.html` (3-4 instanser i Enkel-nivån)
- **bildguide:** `delkapitel/geologi/avsnitt-3-jordbavningar.html` (3 instanser i Enkel-nivån)

**CSS-referens:** `css/geografi.css` — det är denna fil som avgör vad som faktiskt renderas.

När osäker — kolla Geologi **plus** CSS:n.

---

## Revisionshistorik

- **v1.1 (2026-06-17):** Rättad fordj-kort-mall — `<span class="sektion-label">` istället för `<h2>` (verifierat mot CSS efter Code-rapport). Tillagt dokumentationsprincip om HTML-vs-CSS-konflikter.
- **v1.0 (2026-06-17):** Första versionen med fyra komponenter (fordj-kort, brodtext-bild, karnpunkter, bildguide).
