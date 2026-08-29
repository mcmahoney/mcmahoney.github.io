# scripts/bib_to_publications.py
# pip install bibtexparser python-slugify
import bibtexparser
from slugify import slugify
import os

with open('_bibliography/references.bib') as f:
    db = bibtexparser.load(f)

os.makedirs('_publications', exist_ok=True)

for entry in db.entries:
    title = entry.get('title', '').strip('{}')
    year = entry.get('year', '0000')
    date_str = f"{year}-01-01"  # BibTeX often lacks day/month; adjust if you have them
    venue = entry.get('journal', entry.get('booktitle', ''))
    authors = entry.get('author', '').replace(' and ', ', ')
    doi = entry.get('doi', '')
    url = entry.get('url', f"https://doi.org/{doi}" if doi else '')
    slug = slugify(title)[:60]

    citation = f'{authors}. ({year}). "{title}." <i>{venue}</i>.'

    content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{date_str}-{slug}
excerpt: ''
date: {date_str}
venue: '{venue}'
paperurl: '{url}'
citation: '{citation}'
---

{title}
"""
    with open(f"_publications/{date_str}-{slug}.md", 'w') as out:
        out.write(content)

print(f"Generated {len(db.entries)} publication files.")
