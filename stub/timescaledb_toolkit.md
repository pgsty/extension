
--------

## Usage

This extension provide experimental features for timescaledb, check the [docs](https://github.com/timescale/timescaledb-toolkit/tree/main/docs) for details.

## Features

The following links lead to pages for the different features in the TimescaleDB Toolkit repository.

- [ASAP Smoothing](asap.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) - A data smoothing algorithm designed to generate human readable graphs which maintain any erratic data behavior while smoothing away the cyclic noise.
- [Hyperloglog](hyperloglog.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) – An approximate `COUNT DISTINCT` based on hashing that provides reasonable accuracy in constant space. ([Methods](hyperloglog.md#hyperloglog_api))
- [LTTB](lttb.md) [<sup><mark>experimental</mark></sup>](/docs/README.md#tag-notes) – A downsample method that preserves visual similarity. ([Methods](lttb.md#api))

- [Percentile Approximation](percentile_approximation.md) - A simple percentile approximation interface [([Methods](percentile_approximation.md#api))], wraps and simplifies the lower level algorithms:
    - [T-Digest](tdigest.md) – A quantile estimate sketch optimized to provide more accurate estimates near the tails (i.e. 0.001 or 0.995) than conventional approaches. ([Methods](tdigest#tdigest_api))
    - [UddSketch](uddsketch.md) – A quantile estimate sketch which provides a guaranteed maximum relative error. ([Methods](uddsketch.md#uddsketch_api))