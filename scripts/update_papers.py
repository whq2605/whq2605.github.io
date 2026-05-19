#!/usr/bin/env python3
"""
Fetch publications from Google Scholar and update _data/publications.yml.

Preserves manually added entries (e.g., featured: true, pdf paths, code links).
Only adds new papers found on Scholar; does not delete existing entries.

Usage:
    SCHOLAR_ID=WXsYVfsAAAAJ python scripts/update_papers.py
"""

import os
import sys
import time
import yaml
import re
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

SCHOLAR_ID = os.environ.get("SCHOLAR_ID", "WXsYVfsAAAAJ")
PUBLICATIONS_FILE = "_data/publications.yml"
AUTHOR_NAME = "Haiqin Wang"
# Author-name guard: a Scholar entry is only accepted if one of these tokens
# appears in its author list. Using "Haiqin" (not bare "Wang" or "H Wang") so
# that papers by other authors named "Haiqi Wang" / "H. Wang" are rejected.
AUTHOR_NAME_TOKENS = ("Haiqin Wang", "Haiqin W", "H. Wang, X. Xu", "Wang, Haiqin")


def load_existing_publications():
    """Load current publications.yml, ignoring comment-only lines."""
    if not os.path.exists(PUBLICATIONS_FILE):
        return []
    with open(PUBLICATIONS_FILE, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip comment lines before parsing so PyYAML doesn't choke
    cleaned = "\n".join(
        line for line in content.splitlines()
        if not line.strip().startswith("#")
    )
    data = yaml.safe_load(cleaned)
    return data if isinstance(data, list) else []


def normalize_title(title):
    """Lowercase + strip punctuation for fuzzy-matching."""
    return re.sub(r"[^a-z0-9 ]", "", title.lower()).strip()


def fetch_from_scholar():
    """Fetch papers using the scholarly library."""
    try:
        from scholarly import scholarly, ProxyGenerator

        # Try to use SerpAPI if key is available (more reliable)
        serpapi_key = os.environ.get("SERPAPI_KEY", "")
        if serpapi_key:
            pg = ProxyGenerator()
            pg.SerpAPI(serpapi_key)
            scholarly.use_proxy(pg)
            log.info("Using SerpAPI backend for Google Scholar")
        else:
            log.info("Using direct scholarly (no proxy) — may hit rate limits")

        log.info(f"Fetching author profile for Scholar ID: {SCHOLAR_ID}")
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author, sections=["publications"])

        papers = []
        for pub in author.get("publications", []):
            try:
                filled = scholarly.fill(pub)
                bib = filled.get("bib", {})

                # Extract arXiv ID from eprint or URL
                eprint = bib.get("eprint", "")
                pub_url = filled.get("pub_url", "")
                arxiv_id = ""
                if "arxiv.org" in pub_url:
                    m = re.search(r"arxiv\.org/abs/([0-9.]+)", pub_url)
                    if m:
                        arxiv_id = m.group(1)
                elif eprint:
                    arxiv_id = eprint

                author_str = bib.get("author", "")
                # Guard: reject papers where the author list does not contain
                # one of the AUTHOR_NAME_TOKENS. Google Scholar profiles can
                # occasionally include papers by similarly-named authors.
                if not any(tok in author_str for tok in AUTHOR_NAME_TOKENS):
                    log.warning(
                        f"  - Skipped (author guard): {bib.get('title','')[:70]}"
                    )
                    continue

                paper = {
                    "title": bib.get("title", "").strip(),
                    "authors": author_str.replace(
                        AUTHOR_NAME, f"**{AUTHOR_NAME}**"
                    ),
                    "year": int(bib["pub_year"]) if bib.get("pub_year") else None,
                    "journal": bib.get("journal", bib.get("booktitle", bib.get("venue", ""))).strip(),
                    "volume": bib.get("volume", ""),
                    "pages": bib.get("pages", ""),
                    "arxiv": arxiv_id,
                    "doi": bib.get("doi", ""),
                    "url": pub_url,
                    "citations": filled.get("num_citations", 0),
                }
                # Remove empty string values
                paper = {k: v for k, v in paper.items() if v not in ("", None)}
                papers.append(paper)
                time.sleep(1)  # Be polite to Scholar
            except Exception as e:
                log.warning(f"Could not fill publication: {e}")
                continue

        log.info(f"Fetched {len(papers)} papers from Google Scholar")
        return papers

    except Exception as e:
        log.error(f"scholarly fetch failed: {e}")
        return []


def merge_publications(existing, fetched):
    """
    Merge fetched papers into existing list.
    - Preserves all fields in existing entries (featured, pdf, code, etc.)
    - Adds new papers not already in the list
    - Does NOT delete existing entries
    """
    existing_titles = {normalize_title(p["title"]) for p in existing if p.get("title")}

    added = 0
    for paper in fetched:
        norm = normalize_title(paper.get("title", ""))
        if norm and norm not in existing_titles:
            existing.append(paper)
            existing_titles.add(norm)
            added += 1
            log.info(f"  + Added: {paper['title'][:70]}")

    log.info(f"Added {added} new paper(s). Total: {len(existing)}")

    # Sort by year descending, unknown year goes last
    existing.sort(key=lambda p: p.get("year") or 0, reverse=True)
    return existing


def write_publications(pubs):
    header = (
        "# Publications\n"
        "# Auto-updated weekly from Google Scholar via GitHub Actions.\n"
        "# Manual additions (featured, pdf, code) are preserved across updates.\n"
        "#\n"
        "# Field reference:\n"
        "#   title, authors, year, journal, volume, pages\n"
        "#   arxiv (ID only), doi, url, pdf (local path), code (URL)\n"
        "#   featured: true  → shown on home page\n\n"
    )
    with open(PUBLICATIONS_FILE, "w", encoding="utf-8") as f:
        f.write(header)
        yaml.dump(pubs, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)
    log.info(f"Wrote {len(pubs)} publications to {PUBLICATIONS_FILE}")


def main():
    existing = load_existing_publications()
    log.info(f"Loaded {len(existing)} existing publications")

    fetched = fetch_from_scholar()

    if not fetched:
        log.warning("Could not fetch any publications from Google Scholar. Keeping existing file unchanged.")
        sys.exit(0)

    merged = merge_publications(existing, fetched)
    write_publications(merged)


if __name__ == "__main__":
    main()
