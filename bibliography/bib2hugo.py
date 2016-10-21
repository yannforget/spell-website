#!/usr/bin/env python3

import sys
import bibtexparser
import pyaml


def main(bibpath):

    with open(bibpath) as bibfile:
        bibstring = bibfile.read()

    bibdb = bibtexparser.loads(bibstring)

    def reformat_authors(bibfield):
        authors = bibfield.split(' and ')
        lastnames = []
        for i, author in enumerate(authors):
            separated = author.split(', ')
            if len(separated) > 1:
                lastname = separated[0]
                firstname = separated[1]
                if ' van' in firstname.lower():
                    firstname = firstname.replace(' Van', '')
                    firstname = firstname.replace(' van', '')
                    lastname = ' '.join(['Van', lastname])
                if len(firstname) > 3:
                    firstname = '.'.join(
                        [x[0] for x in firstname.replace('-', ' ').split(' ')])
                authors[i] = lastname + ' ' + firstname
            lastnames += [lastname]
        return authors, lastnames

    collection = []
    for article in bibdb.entries:
        data = {}
        data['bibkey'] = article['ID']
        data['itemtype'] = article['ENTRYTYPE']
        if 'title' in article:
            data['title'] = article['title'].replace('{', '').replace('}', '')
        if 'journal' in article:
            data['journal'] = article['journal']
        if 'author' in article:
            data['authors'], data['lastnames'] = reformat_authors(article['author'])
        if 'doi' in article:
            data['doi'] = article['doi'].replace('http://dx.doi.org/', '').replace('dx.doi.org/', '')
        if 'url' in article:
            data['url'] = article['url']
        if 'keyword' in article:
            data['keyword'] = article['keyword'].split(',')
        if 'year' in article:
            data['year'] = article['year']
        if 'volume' in article:
            data['volume'] = article['volume']
        if 'issue' in article:
            data['issue'] = article['issue']
        if 'abstract' in article:
            data['abstract'] = article['abstract']
        collection += [data]

    for article in collection:
        filename = article['bibkey'] + '.md'
        yamlblock = pyaml.dump(article)
        with open(filename, 'w') as md:
            md.write('---\n')
            md.write(yamlblock)
            md.write('---')

if __name__ == '__main__':
    main(sys.argv[1])
