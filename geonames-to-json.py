import argparse
import json

parser = argparse.ArgumentParser(description='Converts geonames cities to JSON suitable for Firebase import')
parser.add_argument('--tsv', metavar='FILE', type=str, help='Path to a geonames TSV export file.')
parser.add_argument('--countries', metavar='COUNTRIES', type=str, help='Comma-separated list of 2-letter country codes. Default: all countries.')
parser.add_argument('--limit', metavar='N', type=int, help='Only use first N matching cities.')

args = parser.parse_args()

countries = []
all_countries = (args.countries == None)
if not all_countries:
    countries = args.countries.split(',')

limit = args.limit
dict = {}

with open(args.tsv) as f:
    for line in f:
        if limit == 0: break

        columns = line.rstrip().split('\t')

        if not all_countries:
            country = columns[8]
            if not country in countries: continue

        id = columns[0]
        name = columns[1]

        dict[id] = {
            'name': name,
        }

        if limit != None:
            limit -= 1

print(json.dumps(dict))
