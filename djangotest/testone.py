#! /usr/bin/env python3

import csv
from datetime import datetime
from dateutil import parser


def read_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    return data


def highest_total_biomass():
    data = read_csv('data.csv')
    record = max(data, key=lambda x: x['Total biomass Fwt (kg)'])
    return '{} at {}'.format(record["Farmers Name"], record['Total biomass Fwt (kg)'])


def lowest_total_biomass():
    data = read_csv('data.csv')
    record = min(data, key=lambda x: x['Total biomass Fwt (kg)'])
    return '{} at {}'.format(record["Farmers Name"], record['Total biomass Fwt (kg)'])


def sort_by_harvest_date():
    data = read_csv('data.csv')
    record = sorted(data[:2], key=lambda x: parser.parse(x['Harvesting date'], dayfirst=True))
    return record


if __name__ == '__main__':
    highest = highest_total_biomass()
    lowest = lowest_total_biomass()
    sorted_by_harvest = sort_by_harvest_date()
