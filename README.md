# Quantifying Breakpoint of SJPD Response

This project analyzes SJPD response times to help quantify the breakpoint of their service.

## Data Source

The data is sourced from the [San Jose Police Calls for Service](https://data.sanjoseca.gov/dataset/police-calls-for-service) dataset.

## Getting Started

```bash
# Setup the environment
uv sync

# Sync the datasets
uv run 00_fetch_sjpd_calls.py
```
