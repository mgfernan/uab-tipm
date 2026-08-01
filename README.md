# TIPM Presentation Scaffold

This repository contains a Quarto-based scaffold for the course presentation of Planning and Management of Telecommunication Infrastructures (TIPM).

## Structure

- `ptig_presentation.qmd`: top-level presentation entry point that assembles the deck from included slide partials.
- `slides/sections/`: shared framing sections such as course overview, methodology, and objectives.
- `slides/sessions/`: one source file per teaching session.
- `assets/`: presentation styling and any future static assets.
- `docs/`: supporting source material, including the subject guide used to derive the scaffold.
- `.vscode/tasks.json`: VS Code tasks for rendering and previewing with workspace-local caches.

## Commands

- Render all configured formats: `quarto render ptig_presentation.qmd`
- Preview the reveal.js deck: `quarto preview ptig_presentation.qmd --no-browser`
- Export a PDF from the rendered deck: open `dist/ptig_presentation.html?print-pdf` in a browser and print to PDF.

Generated output is written to `dist/` and ignored by Git.

## Notes

- The VS Code tasks redirect Quarto and Deno caches to `.cache/` inside the workspace because the container home cache may be read-only.
- The reveal.js theme is styled in `assets/styles.css`, with print-specific adjustments to improve PDF export without requiring a TeX installation.
- Bibliography is configured globally in `_quarto.yml` using `docs/references.bib`, so citations can be used in any slide partial (for example: `[@TripathiReed2025NTN]`).