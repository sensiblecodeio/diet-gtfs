import csv
import sys

# agency.txt done
# routes.txt done, depends on agency.txt
# feed_info.txt done, nothing to change

# calendar_dates.txt depends on service_id.
# shapes.txt depends on trips.txt
# stops.txt depends on stop_times.txt
# stop_times.txt depends on trip_id.
# transfers.txt depends on stop_id from and to, routes.
# trips.txt contains shape_id, also route_id to trip_id.


def clean_agency_from_file(index, filename, *agencies):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[index] in agencies:
                filtered_rows.append(row)

    with open('cleaned/' + filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def filter_routes(*agencies):
    route_ids = set()

    # TODO: Could use cleaned routes.txt?
    with open('routes.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[1] in agencies:
                route_ids.add(row[0])

    print(route_ids)


def main():
    agencies = sys.argv[1:]
    clean_agency_from_file(0, 'agency.txt', *agencies)
    clean_agency_from_file(1, 'routes.txt', *agencies)
    route_ids = filter_routes(*agencies)

if __name__ == '__main__':
    main()
