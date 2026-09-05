from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def prepare_city_data(
    input_path: Path,
    output_path: Path,
    city_name: str,
) -> pd.DataFrame:

    df = pd.read_csv(input_path)

    df.columns = df.columns.str.strip()

    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="coerce",
    )

    temperature_columns = [
        "TAVG",
        "TMAX",
        "TMIN",
    ]

    for column in temperature_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

            df[f"{column}_C"] = (
                df[column] - 32
            ) * 5 / 9

    df["CITY"] = city_name

    df = df.dropna(subset=["DATE"])

    df = df.sort_values("DATE").reset_index(drop=True)

    return df


if __name__ == "__main__":

    tehran = prepare_city_data(
        RAW_DIR / "city_tehran.csv",
        PROCESSED_DIR / "tehran.csv",
        "Tehran",
    )

    sanandaj = prepare_city_data(
        RAW_DIR / "weather_orginal_file.csv",
        PROCESSED_DIR / "sanandaj.csv",
        "Sanandaj",
    )

    tehran.to_csv(
        PROCESSED_DIR / "tehran.csv",
        index=False,
    )

    sanandaj.to_csv(
        PROCESSED_DIR / "sanandaj.csv",
        index=False,
    )

    print("City datasets prepared successfully.")
    print(f"Tehran rows: {len(tehran)}")
    print(f"Sanandaj rows: {len(sanandaj)}")