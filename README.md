# Weather Data Analysis and Visualization

A Python-based data analysis project for cleaning, analyzing, and visualizing weather data from Tehran and Sanandaj, Iran.

## Overview

This project analyzes daily weather observations and compares temperature patterns between Tehran and Sanandaj.

The project demonstrates a basic data analysis pipeline:

Raw Data
→ Data Cleaning
→ Data Transformation
→ Analysis
→ Visualization

## Dataset

The dataset contains daily weather observations including:

- Station
- City
- Date
- Precipitation
- Average Temperature
- Maximum Temperature
- Minimum Temperature

Temperature values in the original dataset are provided in Fahrenheit and are converted to Celsius during preprocessing.

## Project Structure

```text
Weather-Data-Analysis-and-Visualization/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── weather_original.csv
│   │   └── city_tehran.csv
│   │
│   └── processed/
│       ├── weather_cleaned.csv
│       ├── tehran.csv
│       └── sanandaj.csv
│
├── src/
│   ├── cleaning/
│   │   ├── clean_weather.py
│   │   └── prepare_city_data.py
│   │
│   ├── analysis/
│   │   └── city_comparison.py
│   │
│   └── visualization/
│       ├── temperature_tehran.py
│       ├── temperature_sanandaj.py
│       └── compare_cities.py
│
├── outputs/
│   └── figures/
│
└── notebooks/