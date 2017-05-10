import csv
import sys

# agency.txt done
# feed_info.txt nothing to change

# calendar_dates.txt depends on service_id.
# routes.txt depends on agency.txt
# shapes.txt depends on trips.txt
# stops.txt depends on stop_times.txt
# stop_times.txt depends on trip_id.
# transfers.txt depends on stop_id from and to, routes.
# trips.txt contains shape_id, also route_id to trip_id.


def clean_agency_file(*agencies):
    with open('agency.txt', 'r') as f:
        reader = csv.reader(f)
        filtered_rows = []
        filtered_rows.append(next(reader))

        for row in reader:
            if row[0] in agencies:
                filtered_rows.append(row)

    with open('cleaned/agency.txt', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(filtered_rows)


def main():
    agencies = sys.argv[1:]
    clean_agency_file(*agencies)


if __name__ == '__main__':
    main()
