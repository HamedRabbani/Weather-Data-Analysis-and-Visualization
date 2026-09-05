from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA = BASE_DIR / "data" / "raw" / "weather_orginal_file.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def fahrenheit_to_celsius(series: pd.Series) -> pd.Series:
    """Convert Fahrenheit temperatures to Celsius."""
    return (series - 32) * 5 / 9


def clean_weather_data(input_path: Path) -> pd.DataFrame:
    """Load and clean the raw weather dataset."""

    df = pd.read_csv(input_path)

    required_columns = [
        "STATION",
        "NAME",
        "DATE",
        "TAVG",
        "TMAX",
        "TMIN",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Normalize column names
    df.columns = df.columns.str.strip()

    # Parse dates
    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="coerce",
    )

    # Convert temperature columns to numeric
    temperature_columns = ["TAVG", "TMAX", "TMIN"]

    for column in temperature_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    # Remove rows without valid dates
    df = df.dropna(subset=["DATE"]).copy()

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Convert Fahrenheit to Celsius
    for column in temperature_columns:
        df[f"{column}_C"] = fahrenheit_to_celsius(
            df[column]
        )

    # Sort chronologically
    df = df.sort_values("DATE").reset_index(drop=True)

    return df


if __name__ == "__main__":
    cleaned_df = clean_weather_data(RAW_DATA)

    output_path = PROCESSED_DIR / "weather_cleaned.csv"

    cleaned_df.to_csv(
        output_path,
        index=False,
    )

    print(f"Cleaned dataset saved to: {output_path}")
    print(f"Rows: {len(cleaned_df)}")
    print("\nMissing values:")
    print(
        cleaned_df[
            ["DATE", "TAVG_C", "TMAX_C", "TMIN_C"]
        ].isna().sum()
    )