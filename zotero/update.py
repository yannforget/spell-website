#!/usr/bin/env python3
"""Take input references exported from Zotero as
CSV files and process them to .JSON so that they
can be used in the Hugo templates.
"""

import csv
import json
import os

# Zotero keys to keep in the final .json file
# and their new name (for compatibility with Hugo).
KEYS = {
    'Item Type': 'itemType',
    'Publication Year': 'publicationYear',
    'Author': 'publicationAuthors',
    'Title': 'publicationTitle',
    'Publication Title': 'journal',
    'ISBN': 'isbn',
    'ISSN': 'issn',
    'DOI': 'doi',
    'Pages': 'pages',
    'Issue': 'issue',
    'Volume': 'volume',
    'Publisher': 'publisher',
    'Place': 'place',
    'Manual Tags': 'zoteroTags',
    'Editor': 'editor',
    'Proceedings Title': 'proceedingsTitle',
    'Conference Name': 'conferenceName',
    'Book Title': 'bookTitle',
    'Url': 'publicationUrl',
    'Type': 'thesisType',
    'external': 'external',
}


def get_initials(first_name):
    """Format first name to consistently retrieve the initials.
    `Marius` becomes `M.`, `Jean-Claude` becomes `J.-C.`,
    `Andrew Junior` becomes `A. J.`, etc.
    """
    initials = []
    if '-' in first_name:
        first_name = first_name.replace(' ', '')
    name_parts = first_name.split()
    for part in name_parts:
        if '-' in part:
            separated = part.split('-')
            initials.append(separated[0][0] + '.-' + separated[1][0] + '.')
        elif '.' in part:
            separated = part.split('.')
            for sep in separated:
                if sep:
                    initials.append(sep[0] + '.')
        else:
            initials.append(part[0] + '.')
    return ' '.join(initials)


def format_authorship(raw):
    """Format authorship as exported from Zotero.
    Also make sure that first names are all abbreviated.

    Parameters
    ----------
    raw : str
        Raw authorship string from Zotero.

    Returns
    -------
    authorship : list
        Formatted authorship as a list.
    """
    authorship = []
    for author in raw.split(';'):
        splitted_names = author.split(',')
        if len(splitted_names) == 2:
            last_name, first_name = splitted_names
            last_name = last_name.strip()
            first_name = first_name.strip()
            first_name = get_initials(first_name)
            authorship.append(first_name + ' ' + last_name)
        elif len(splitted_names) == 1:
            authorship.append(splitted_names[0])
    return authorship


def format_doi(raw):
    """Format DOI string for consistency by making sure that
    the full dx.doi.org is not included.
    """
    doi = raw.replace('http://dx.doi.org/', '')
    doi = doi.replace('dx.doi.org/', '')
    return doi


def format_reference(raw):
    """Format the input reference.

    Parameters
    ----------
    raw : dict
        Input reference.

    Returns
    -------
    reference : dict
        Formatted reference.
    """
    reference = {}
    for key in KEYS:
        dst_key = KEYS[key]
        if key in raw:
            if key == 'Author':
                reference[dst_key] = format_authorship(raw[key])
            elif key == 'Editor':
                reference[dst_key] = format_authorship(raw[key])
            elif key == 'DOI':
                reference[dst_key] = format_doi(raw[key])
            else:
                reference[dst_key] = raw[key]
    return reference


def write_json(references, destination):
    """Write the formatted references as a .json file.

    Parameters
    ----------
    references : list of dict
        Formatted references.
    destination : str
        Path to the output .json file.
    """
    if os.path.isfile(destination):
        os.remove(destination)
    with open(destination, 'w') as f:
        json.dump(references, f, indent=True)


def update(zotero_dir, destination):
    """Update..."""
    csv_files = [
        os.path.join(zotero_dir, f)
        for f in os.listdir(zotero_dir)
        if f.endswith('.csv')
    ]

    raw_references = []
    for csv_f in csv_files:
        external = 'external' in csv_f
        f = open(csv_f)
        reader = csv.DictReader(f)
        for row in reader:
            row['external'] = external
            raw_references.append(row)
        f.close()

    references = []
    for raw in raw_references:
        # Try to format each reference. If it fails, just log
        # the title of the reference for correction in Zotero.
        try:
            references.append(format_reference(raw))
        except:
            print('Cannot process "{}"'.format(raw['Title']))

    write_json(references, destination)


if __name__ == '__main__':
    ZOTERO_DIR = os.path.abspath(os.path.dirname(__file__))
    DESTINATION = os.path.join(
        ZOTERO_DIR, '..', 'data', 'publications', 'references.json')
    update(ZOTERO_DIR, DESTINATION)
