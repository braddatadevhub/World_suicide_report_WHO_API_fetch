# World Suicide Data Report (WHO API)

This project implements a **Python-based data ingestion and transformation pipeline** to retrieve global suicide rate data from the World Health Organization (WHO) public API.

The workflow fetches structured JSON data, enriches it with country metadata, and produces an **analysis-ready dataset** suitable for reporting, research, or visualization.

---

## Features

- Retrieves suicide rate data from the WHO Global Health Observatory API
- Consumes structured JSON responses
- Enriches records with country and regional metadata
- Cleans and normalizes numeric values
- Produces a sorted, analysis-ready dataset
- Exports final results to CSV format

---

## Data Source

- **World Health Organization (WHO) – Global Health Observatory API**
- Indicator: Suicide mortality rate
- Coverage: Global
- Records retrieved based on most recent data available at time of extraction

---

## Project Workflow

### 1. Extract
- Fetches suicide rate data using the WHO API
- Retrieves country and regional metadata from a reference endpoint
- Validates successful API responses

### 2. Transform
- Converts indicator values to numeric format
- Sorts records by year (most recent first)
- Maps country codes to human-readable country names
- Enriches records with regional classifications
- Formats values consistently for analytical use

### 3. Load
- Exports the processed dataset to CSV format
- Produces a structured file ready for analysis or visualization tools

---

## Technologies Used

- Python
- Requests
- Pandas

---

## Output

The final dataset includes:
- Country
- Region
- Year
- Suicide rate

All numeric fields are validated and formatted for analytical workflows.

---

## Use Cases

- Public health and demographic analysis
- API-based data ingestion demonstrations
- ETL and data enrichment pipelines
- Dashboarding and reporting workflows
- Research and statistical analysis foundations

---

## Notes

This project emphasizes:
- Reliable API consumption
- Data enrichment through reference datasets
- Clean, analysis-ready output

The pipeline can be extended to:
- Support additional health indicators
- Persist data to databases or cloud storage
- Run as part of scheduled or automated workflows

---

## Author

Developed by **BRADLEY**
