# Foundry VTT v13 — Importing the GM Guide Journal

Companion file: [`dawn-of-the-jedaii.journal.json`](dawn-of-the-jedaii.journal.json)

Generated from the master Markdown book via:

```bash
python tools/md_to_foundry_journal.py
```

Each `#` heading in `dawn-of-the-jedaii-campaign-guide.md` becomes one Journal Entry **page** using Markdown format (`text.format: 2`) and the Markdown page sheet.

## Import (UI)

1. Open your Foundry VTT **v13** world (SW5e).
2. Open the **Journal Entries** directory.
3. Create a new Journal Entry (name can be temporary).
4. Right-click that entry → **Import Data**.
5. Choose `foundry/dawn-of-the-jedaii.journal.json`.
6. Confirm. The entry should rename to **Dawn of the Je'daii — GM Guide** and list chapter pages.

Alternatively: in the Journal directory, use any existing entry’s Import Data after placing the JSON where you can browse to it.

## If pages appear blank after import

Foundry sometimes stores Markdown in `text.markdown` but leaves `text.content` empty until the page is saved once. Fix options:

### A — Re-save in the UI

Open each blank page, switch to the Markdown sheet if needed, and save (Ctrl+S).

### B — One-shot console snippet

Paste into the Foundry client console (`F12`), then reload the journal:

```js
const name = "Dawn of the Je'daii — GM Guide";
const journal = game.journal.getName(name);
if (!journal) {
  ui.notifications.error(`Journal not found: ${name}`);
} else {
  const updates = [];
  for (const page of journal.pages) {
    const md = page.text?.markdown;
    if (md && page.text?.format === 2) {
      updates.push({ _id: page.id, "flags.core.sheetClass": "core.MarkdownJournalPageSheet" });
    }
  }
  if (updates.length) {
    await journal.updateEmbeddedDocuments("JournalEntryPage", updates);
    ui.notifications.info(`Touched ${updates.length} markdown pages. Open/save any still-blank page once.`);
  }
}
```

If a page is still blank, open it and save once so Foundry regenerates HTML `content` from Markdown.

## Permissions

Keep this journal **GM-only** (default ownership 0). Copy **Appendix C — Handouts & Player Primer** into a separate player-visible journal if you want a safe handout.

## Regenerating after edits

1. Edit `dawn-of-the-jedaii-campaign-guide.md` (keep one `#` title per chapter).
2. Run `python tools/md_to_foundry_journal.py`.
3. Re-import over the journal (or delete and import fresh).
