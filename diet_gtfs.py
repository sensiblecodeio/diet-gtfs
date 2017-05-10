import csv
import sys


def clean_agency_file(*agencies):
    with open('agency.txt', 'r') as f:
        reader = csv.reader(f)
        next(f)
        for row in reader:
            if row[0] in agencies:
                print(row)


def main():
    agencies = sys.argv[1:]
    clean_agency_file(*agencies)


if __name__ == '__main__':
    main()
