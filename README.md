# whq2605.github.io — Haiqin Wang's Personal Website

Personal academic website for Haiqin Wang, Postdoc Research Scholar at Harvey Mudd College.

## Structure

```
├── index.md                  # Home / About page
├── _pages/
│   ├── research.md           # Research projects
│   ├── publications.md       # Full publication list
│   ├── teaching.md           # Teaching experience
│   └── notes.md              # Shared notes & resources
├── _data/
│   ├── publications.yml      # Publication entries (auto-updated)
│   └── projects.yml          # Research project descriptions
├── _layouts/                 # Jekyll HTML layouts
├── _includes/                # Reusable HTML partials
├── assets/
│   ├── css/main.css          # Custom stylesheet
│   ├── img/profile.jpg       # Profile photo
│   └── pdf/                  # CV and paper PDFs
├── scripts/
│   └── update_papers.py      # Google Scholar scraper
└── .github/workflows/
    └── update-papers.yml     # Weekly auto-update action
```

## Editing content

### Update your bio
Edit `index.md` — the "About Me" section and news items are plain Markdown/HTML.

### Add a new publication manually
Edit `_data/publications.yml` and add an entry:
```yaml
- title: "Your Paper Title"
  authors: "Co-author A, **Haiqin Wang**, Co-author B"
  year: 2025
  journal: "Physical Review Letters"
  arxiv: "2501.12345"
  doi: "10.1103/PhysRevLett.xxx"
  pdf: /assets/pdf/paper_name.pdf
  code: https://github.com/whq2605/repo-name
  featured: true   # show on home page
```

### Add a research project
Edit `_data/projects.yml` and add a new block (copy an existing one as template).

### Add notes/resources
Edit `_pages/notes.md` — copy one of the existing `.note-card` blocks.

### Add teaching entries
Edit `_pages/teaching.md` — copy one of the existing `.course-item` blocks.

### Upload CV
Place your CV PDF at `assets/pdf/CV.pdf`.

## Automatic publication updates

The GitHub Action `.github/workflows/update-papers.yml` runs every Sunday and:
1. Calls Google Scholar (Scholar ID: `WXsYVfsAAAAJ`)
2. Merges any new papers into `_data/publications.yml`
3. Commits the change (which triggers a GitHub Pages rebuild)

**Manually trigger**: Go to Actions tab → "Update Publications" → "Run workflow".

**More reliable scraping**: Add a `SERPAPI_KEY` secret in your repo settings
(Settings → Secrets → Actions) to use SerpAPI as the Scholar backend.

## Local development

```bash
bundle install
bundle exec jekyll serve --livereload
```

Then open http://localhost:4000.
