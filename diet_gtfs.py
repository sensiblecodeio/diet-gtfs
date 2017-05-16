#!/usr/bin/env python3
from collections import Counter
from decimal import Decimal
import csv
import sys


def process_trips(trip_ids):
    route_ids = set()
    shape_ids = set()
    service_ids = set()

    with open('trips.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[2] in trip_ids:
                filtered_rows.append(row)
                route_ids.add(row[0])
                shape_ids.add(row[9])
                service_ids.add(row[1])

    with open('cleaned/trips.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)

    return route_ids, shape_ids, service_ids


def clean_shapes(shape_ids):
    with open('shapes.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in shape_ids:
                filtered_rows.append(row)

    with open('cleaned/shapes.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def process_stop_times(stop_ids):
    trip_ids = set()

    trip_id_count = Counter()

    with open('stop_times.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[2] in stop_ids:
                filtered_rows.append(row)
                trip_id_count[row[0]] += 1

        for trip_id, count in trip_id_count.items():
            if count >= 2:
                trip_ids.add(trip_id)

        cleaned_rows = [filtered_rows[0]]

        for row in filtered_rows[1:]:
            if row[0] in trip_ids:
                cleaned_rows.append(row)

    with open('cleaned/stop_times.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)

    return trip_ids


def process_stops(min_lat, max_lat, min_lon, max_lon):
    stop_ids = set()

    with open('stops.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            stop_lat = Decimal(row[3])
            stop_lon = Decimal(row[4])
            if (stop_lat >= min_lat and stop_lat <= max_lat
                    and stop_lon >= min_lon and stop_lon <= max_lon):
                filtered_rows.append(row)
                stop_ids.add(row[0])

    with open('cleaned/stops.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)

    return stop_ids


def process_routes(route_ids):
    agency_ids = set()

    with open('routes.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in route_ids:
                filtered_rows.append(row)
                agency_ids.add(row[1])

    with open('cleaned/routes.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)

    return agency_ids


def clean_transfers(stop_ids, trip_ids):
    with open('transfers.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if (row[0] in stop_ids and row[1] in stop_ids
                and row[4] in trip_ids and row[5] in trip_ids):
                filtered_rows.append(row)

    with open('cleaned/transfers.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def clean_calendar(service_ids):
    with open('calendar_dates.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in service_ids:
                filtered_rows.append(row)

    with open('cleaned/calendar_dates.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def clean_agencies(agency_ids):
    with open('agency.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in agency_ids:
                filtered_rows.append(row)

    with open('cleaned/agency.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def main():
    min_lat_str, max_lat_str, min_lon_str, max_lon_str = sys.argv[1:5]
    min_lat = Decimal(min_lat_str)
    max_lat = Decimal(max_lat_str)
    min_lon = Decimal(min_lon_str)
    max_lon = Decimal(max_lon_str)

    # TODO: Deduplicate code.
    stop_ids = process_stops(min_lat, max_lat, min_lon, max_lon)
    trip_ids = process_stop_times(stop_ids)
    route_ids, shape_ids, service_ids = process_trips(trip_ids)
    agency_ids = process_routes(route_ids)
    clean_transfers(stop_ids, trip_ids)
    clean_shapes(shape_ids)
    clean_calendar(service_ids)
    clean_agencies(agency_ids)


if __name__ == '__main__':
    main()
