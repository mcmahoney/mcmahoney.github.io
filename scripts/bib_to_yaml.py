import bibtexparser, yaml

with open('_bibliography/references.bib') as f:
    db = bibtexparser.load(f)

pubs = [{
    'title': e.get('title', '').strip('{}'),
    'authors': e.get('author', ''),
    'year': e.get('year', ''),
    'journal': e.get('journal', e.get('booktitle', '')),
    'url': e.get('url', ''),
    'doi': e.get('doi', ''),
} for e in db.entries]

pubs.sort(key=lambda x: x['year'], reverse=True)

with open('_data/publications.yml', 'w') as out:
    yaml.dump(pubs, out, allow_unicode=True, sort_keys=False)
