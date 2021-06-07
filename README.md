# geonames-to-json

This script picks cities from GeoNames DB files in TSV format and writes JSON output.

Usage:
```
python3 geonames-to-json.py [-h] [--tsv FILE] [--countries COUNTRIES] [--limit N]
```
Converts geonames cities to JSON suitable for Firebase import

optional arguments:
-  `-h`, `--help`            show this help message and exit
-  `--tsv FILE`            Path to a geonames TSV export file.
-  `--countries COUNTRIES` Comma-separated list of 2-letter country codes. Default: all countries.
-  `--limit N`             Only use first N matching cities.

Example:
```bash
python3 geonames-to-json.py --tsv cities500.txt --countries GB -- limit 3 > gb.json
```

Output:
```json
{"146839": {"name": "Akrotiri"}, "2633332": {"name": "Ystrad Mynach"}, "2633334": {"name": "Ystradgynlais"}}
```

## TODO
- Pick fields.

## Firebase Import
In case you want to import this JSON to Firebase, use this:

```bash
npm install -g node-firestore-import-export
firestore-import --accountCredentials credentials.json --backupFile gb.json --nodePath ukCities
```

where `credentials.json` is a file you export from Firebase console as per this tutorial: https://www.youtube.com/watch?v=gPzs6t3tQak
