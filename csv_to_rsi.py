#!/usr/bin/env python
# To use:
# csv_to_rsi.py csvfile.csv

import csv
from sys import argv

inputfile = argv[1]  # csv file

# csv header to rsi mapping; order does not matter
csv_to_rsi = {'title': 'TI', 'authors': 'AU', 'abstract': 'AB',
              'published year': 'PY', 'journal': 'JO', 'volume': 'VL',
              'issue': 'IS', 'accession number': 'AN', 'doi': 'DO'}
headers = None

with open(inputfile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        # skip empty rows
        if row[0] == '':
            continue
        # assume first row is headers and set them
        if not headers:
            headers = {k.lower(): v for v, k in enumerate(row)}
            continue

        print(f"TY - JOUR")
        for key in csv_to_rsi:
            if key == 'authors':
                authors = row[headers.get(key)].split(';')
                for author in authors:
                    print(f"{csv_to_rsi[key]} - {author.lstrip()}")
            else:
                print(f"{csv_to_rsi[key]} - {row[headers.get(key)]}")
        print(f"ER - ")
