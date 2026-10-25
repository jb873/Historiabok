# Arbetsorder — Wienkongressen: två kartor in i texten

**Repo:** Historiabok · **Datum:** 2026-10-25
**Gäller:** `kapitel/vagen-till-forsta-varldskriget/delkapitel/wienkongressen/avsnitt-1-wienkongressen.html`

## 1. Leverans
Lägg de två uppdaterade innehållsfilerna i `doc/leveranser/vtfvk-wienkongressen/innehall/` (ersätter A och C där; föregående versioner ligger i `versioner/` i leveransen):
- `A-europa-efter-napoleon.md`
- `C-maktbalans-europas-nya-karta.md`

## 2. Bilder
| Karta | Nytt filnamn i `delkapitel/wienkongressen/img/` | Underdel |
|---|---|---|
| Karta 1 – Europa 1815, stormakterna med Wien | `wien-stormakterna-1815.webp` | A |
| Karta 3 – Centraleuropa | `wien-centraleuropa-1815.webp` | C |
| Karta 2 – Europa 1815, en ny ordning | används inte i texten, ligger kvar i `kartor-2026-10-25/` | – |

Rätta etiketten "Preussen" i karta 3 innan den kopieras. Skala ned båda till samma bredd som övriga bilder i delkapitlet och spara som webp.

## 3. Vad som ändras
- **A:** fyrrutebilden **flyttas** från slutet av "Wienkongressen – stormakterna bestämmer" till slutet av "Napoleon besegras – Europa behöver en ny ordning". Kartan läggs in efter stycket om de fem stormakterna. Ny bildguide 2 på Enkel.
- **C:** ringkartan står kvar. Centraleuropakartan läggs in efter stycket om Italien under "Tyskland och Italien förblir splittrade". Ny bildguide 2 på Enkel.
- Båda kartorna får samma källrad under bildtexten som ringkartan.

## 4. Nytt i innehållsfilerna
Filerna har nu **två** BILD-block (`## BILD 1 …`, `## BILD 2 …`), två bildguider (`### Bildguide 1`, `### Bildguide 2`) och numrerade markeringar: `[BILDGUIDE 1 + BILD 1 HÄR]`, `[BILDGUIDE 2 + BILD 2 HÄR]`, `[BILD 1 HÄR]`, `[BILD 2 HÄR]`. Bildguide N hör till bild N. Generatorn behöver hantera numren; i övrigt gäller samma regler som tidigare. Kontrollera att rubrikraderna "Bildguide 1/2 …" inte syns på sidan.

## 5. Verifiering (headless Chromium)
Samma 45 kontroller som tidigare, plus:
1. A och C har två bilder på Enkel och Standard, i rätt ordning och på rätt plats, ingen bild på Fördjupning.
2. Varje bildguide står direkt före sin egen bild.
3. B och D är oförändrade.
4. Skärmdumpar: Enkel A och Standard C.

## 6. Ramar
Skriv inte över tidigare filer utan att de finns kvar i `versioner/`. Rör inte `Arkiv/` eller `ideologier`. Vänta med push tills Joachim säger till.
