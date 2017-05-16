# diet-gtfs

Trim your GTFS feeds down to a suitable fighting weight for battling with
transit data, based on selecting a lat/lon "rectangle".

## Why?

We're currently interested in providing only a small part of a large
countrywide GTFS feed, for collaborators on a project using
OpenTripPlanner.

Unfortunately, large GTFS feeds are currently [slow to load in
OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner/issues/2063).

Tools such as the [onebusaway
transformer](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/1.3.3/onebusaway-gtfs-transformer-cli.html)
exist, but they can be very slow to process large feeds, even to do
something like [throwing the bulk of the data
away](http://www.stevenmaude.co.uk/posts/trying-to-trim-down-static-gtfs-feeds).

## What?

This is a simple Python 3 module that loads in an unzipped GTFS feed,
and outputs trimmed files that contain only details for a region inside
a lat/lon "rectangle".

It currently needs an output directory `cleaned` creating.

It's using the standard library only, so no external requirements.

Right now, it's hardcoded to this [Netherlands GTFS
feed](http://gtfs.ovapi.nl/new/) (see this
[issue](https://github.com/sensiblecodeio/diet-gtfs/issues/4) which
needs resolving). In the meantime, you could adjust the column index
numbers to match the appropriate columns in your files.

## How?

`python3 diet_gtfs.py min_lat max_lat min_lon max_lon`

e.g.

`python3 diet_gtfs.py 51.3 51.5 5.3 5.8`
