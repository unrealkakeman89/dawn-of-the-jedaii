# Foundry VTT v13 — Importing the GM Guide Journal

Companion file: [`dawn-of-the-jedaii.journal.json`](dawn-of-the-jedaii.journal.json)

Generated from the master Markdown book via:

```bash
pip install -r requirements.txt
python tools/md_to_foundry_journal.py
```

Each `#` heading in `dawn-of-the-jedaii-campaign-guide.md` becomes one Journal Entry **page** with:

- `text.format: 2` (Markdown) + `text.markdown` (source)
- `text.content` (pre-rendered HTML — **required for display**)
- Markdown page sheet flag

Foundry’s Import Data path does **not** compile Markdown into HTML. Without `text.content`, page titles list correctly but bodies stay blank (including under **Monk’s Enhanced Journal**). The exporter always writes both.

## Import (UI)

1. Open your Foundry VTT **v13** world (SW5e).
2. Open the **Journal Entries** directory.
3. Create a new Journal Entry (name can be temporary), **or** delete the old empty-looking **Dawn of the Je'daii — GM Guide** entry first.
4. Right-click that entry → **Import Data**.
5. Choose `foundry/dawn-of-the-jedaii.journal.json`.
6. Confirm. The entry should rename to **Dawn of the Je'daii — GM Guide** and list chapter pages with visible body text.

Alternatively: in the Journal directory, use any existing entry’s Import Data after placing the JSON where you can browse to it.

## If pages still appear blank

Usually this means an **older import** that only had `text.markdown` and no `text.content`. Prefer **delete + re-import** the regenerated JSON.

### Console heal (already-imported journal)

Paste into the Foundry client console (`F12`), then reopen the journal:

```js
const name = "Dawn of the Je'daii — GM Guide";
const journal = game.journal.getName(name);
if (!journal) {
  ui.notifications.error(`Journal not found: ${name}`);
} else {
  const updates = [];
  for (const page of journal.pages) {
    const md = page.text?.markdown;
    if (!md) continue;
    let html = page.text?.content;
    if (!html || !String(html).trim()) {
      if (typeof showdown !== "undefined") {
        html = new showdown.Converter({ tables: true, strikethrough: true }).makeHtml(md);
      } else {
        ui.notifications.warn(`No Showdown converter; re-import the JSON for page ${page.name}`);
        continue;
      }
    }
    updates.push({
      _id: page.id,
      "text.content": html,
      "flags.core.sheetClass": "core.MarkdownJournalPageSheet",
    });
  }
  if (updates.length) {
    await journal.updateEmbeddedDocuments("JournalEntryPage", updates);
    ui.notifications.info(`Healed ${updates.length} pages (wrote text.content). Reopen the journal.`);
  } else {
    ui.notifications.warn("No pages updated. Re-import foundry/dawn-of-the-jedaii.journal.json.");
  }
}
```

Monk’s Enhanced Journal renders `text.content` HTML. Titles alone are not enough.

## Permissions

Keep this journal **GM-only** (default ownership 0). Copy **Appendix C — Handouts & Player Primer** into a separate player-visible journal if you want a safe handout.

## Regenerating after edits

1. Edit `dawn-of-the-jedaii-campaign-guide.md` (keep one `#` title per chapter).
2. Run `pip install -r requirements.txt` once, then `python tools/md_to_foundry_journal.py`.
3. Re-import over the journal (or delete and import fresh).
