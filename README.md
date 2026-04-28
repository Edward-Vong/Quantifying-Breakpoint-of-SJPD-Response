# Quantifying Breakpoint of SJPD Response

This project analyzes SJPD response times to help quantify the breakpoint of their service.

## Data Source

The data is sourced from the [San Jose Police Calls for Service](https://data.sanjoseca.gov/dataset/police-calls-for-service) dataset.

## Getting Started

### 1. Environment Setup

```bash
uv sync
```

### 2. Data Synchronization
Synchronize datasets and refresh the current year:

```bash
uv run scripts/sync_data.py
```

 