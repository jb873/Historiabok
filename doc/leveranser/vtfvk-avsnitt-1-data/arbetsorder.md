# Arbetsorder — VTFVK avsnitt 1: JSON-data

**Repo:** Historiabok · **Datum:** 2026-09-27
**Styrdokument:** LEVERANSGUIDE DEL 3–6 (scheman)

## 1. Syfte
Lägga in datafilerna för avsnitt 1 (Nationalism) så att Öva- och Elevboken-flikarna fungerar. Inget annat byggs.

## 2. Leverans
Lägg leveransen i `doc/leveranser/vtfvk-avsnitt-1-data/` och committa den. Kopiera därifrån:

| Leveransfil | Mål i repot |
|---|---|
| `data/fragor.json` | `kapitel/vagen-till-forsta-varldskriget/data/fragor.json` |
| `data/begreppsbank.json` | `kapitel/vagen-till-forsta-varldskriget/data/begreppsbank.json` |
| `data/matris.json` | `kapitel/vagen-till-forsta-varldskriget/data/matris.json` |
| `data/flipcards/avsnitt-1-nationalism.json` | `kapitel/vagen-till-forsta-varldskriget/data/flipcards/avsnitt-1-nationalism.json` |

Inga befintliga filer skrivs över (mappen `data/` innehåller i dag bara `avsnittslista-ideologier.json`).

## 3. Kontrollera först, rapportera avvikelser
1. **Rotfältet `delkapitel` i flipcards-filen** är satt till `"ideologier"`. Kontrollera vilket värde befintliga Historia-flipcards (t.ex. Medeltiden) använder: delkapitel-id eller kapitel-id. Följ befintligt mönster och rapportera om du ändrar.
2. **`kallfil` i begreppsbanken** är `data/flipcards/avsnitt-1-nationalism.json` (relativt kapitlet). Kontrollera mot befintliga begreppsbanker och följ deras mönster.
3. `fragor.json` har rot-`delkapitel` = kapitel-id enligt LEVERANSGUIDE DEL 3. Kontrollera mot Medeltiden.

## 4. Verifiering (headless Chromium)
1. Öva-fliken laddar 32 kort: 17 begreppskort, 10 modellkort, 5 redogörelsekort. Markdown i modellsvaren renderas (fetstil, stycken).
2. Elevboken visar 11 frågor utan felmeddelande. Konsolen har inte längre felet om fragor.json.
3. Föreläsningsfliken är fortfarande inaktiv (förväntat).
4. Skärmdumpar: Öva med ett vänt modellkort, Elevboken.

Begreppsbanken och matrisen används av kapitelverktygen, som byggs senare. Verifiera bara att filerna är giltig JSON.

## 5. Ramar
Skriv inte över befintliga filer. Rör inte `Arkiv/`. Uppfinn inga fält. Git-commit per steg.
