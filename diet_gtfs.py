import csv
import sys

# agency.txt done
# routes.txt done, depends on agency.txt
# feed_info.txt done, nothing to change
# trips.txt contains shape_id, also route_id to trip_id.
# shapes.txt depends on trips.txt
# stop_times.txt depends on trip_id.
# stops.txt depends on stop_times.txt
# transfers.txt depends on stop_id from and to, routes.
# calendar_dates.txt depends on service_id.


def clean_agency_from_file(index, filename, *agencies):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        # TODO: consider writing files per row, not storing all first.
        for row in reader:
            if row[index] in agencies:
                filtered_rows.append(row)

    with open('cleaned/' + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def get_route_ids(*agencies):
    route_ids = set()

    # TODO: Could use cleaned routes.txt?
    with open('routes.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] in agencies:
                route_ids.add(row[0])

    return route_ids


def clean_trips(route_ids):
    with open('trips.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in route_ids:
                filtered_rows.append(row)

    with open('cleaned/trips.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


# TODO: Deduplicate?
def get_ids_from_trips(route_ids):
    trip_ids = set()
    shape_ids = set()
    service_ids = set()

    with open('trips.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] in route_ids:
                trip_ids.add(row[2])
                shape_ids.add(row[9])
                service_ids.add(row[1])

    return trip_ids, shape_ids, service_ids


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


def clean_stop_times(trip_ids):
    with open('stop_times.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in trip_ids:
                filtered_rows.append(row)

    with open('cleaned/stop_times.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def get_stop_ids(trip_ids):
    stop_ids = set()

    with open('stop_times.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] in trip_ids:
                stop_ids.add(row[2])

    return stop_ids


def clean_stops(stop_ids):
    with open('stops.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in stop_ids:
                filtered_rows.append(row)

    with open('cleaned/stops.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def clean_transfers(stop_ids):
    with open('transfers.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in stop_ids and row[1] in stop_ids:
                filtered_rows.append(row)

    with open('cleaned/transfers.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def get_service_ids(trip_ids):
    service_ids = set()

    with open('stop_times.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] in trip_ids:
                service_ids.add(row[2])

    return service_ids


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


def main():
    agencies = sys.argv[1:]
    clean_agency_from_file(0, 'agency.txt', *agencies)
    clean_agency_from_file(1, 'routes.txt', *agencies)
    route_ids = get_route_ids(*agencies)
#    print("Route ids:", route_ids)
    clean_trips(route_ids)
    trip_ids, shape_ids, service_ids = get_ids_from_trips(route_ids)
#    print("Trip ids:", trip_ids)
#    print("Shape ids:", shape_ids)
    clean_shapes(shape_ids)
    clean_stop_times(trip_ids)
    stop_ids = get_stop_ids(trip_ids)
    clean_stops(stop_ids)
    clean_transfers(stop_ids)
    clean_calendar(service_ids)

if __name__ == '__main__':
    main()
