![a kraken](https://raw.githubusercontent.com/netkraken/minion/master/res/octopus.png)

# countdb

[![Build Status](https://api.travis-ci.org/netkraken/countdb.svg?branch=master)](https://travis-ci.org/netkraken/countdb)
[![Coverage Status](https://coveralls.io/repos/netkraken/countdb/badge.svg)](https://coveralls.io/r/netkraken/countdb)
[![PyPI version](https://badge.fury.io/py/countdb.svg)](http://badge.fury.io/py/countdb)

count events with arbitrary names, over time, aggregates minutes/hours/days

## tl;dr
* counts events with arbitrary names
* stores events per minute (averaging multiple measurements)
* aggregates events per hour/day

## API: CountDB

```open(filename)```
opens the CountDB readonly

```open_for_counting(filename)```
constitutes a single measurement, stored in a CountDB, allows multiple calls to ```count(key)```

```open_for_extending(filename)```
merges another CountDB with the current one (used for the aggregation)
