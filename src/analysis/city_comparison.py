from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def temperature_summary(
    df: pd.DataFrame,
    city: str,
) -> pd.DataFrame:

    summary = {
        "City": city,
        "Average_TMAX_C": df["TMAX_C"].mean(),
        "Maximum_TMAX_C": df["TMAX_C"].max(),
        "Minimum_TMAX_C": df["TMAX_C"].min(),
        "Average_TMIN_C": df["TMIN_C"].mean(),
        "Maximum_TMIN_C": df["TMIN_C"].max(),
        "Minimum_TMIN_C": df["TMIN_C"].min(),
    }

    return pd.DataFrame([summary])


def main():

    tehran = pd.read_csv(
        PROCESSED_DIR / "tehran.csv"
    )

    sanandaj = pd.read_csv(
        PROCESSED_DIR / "sanandaj.csv"
    )

    tehran_summary = temperature_summary(
        tehran,
        "Tehran",
    )

    sanandaj_summary = temperature_summary(
        sanandaj,
        "Sanandaj",
    )

    comparison = pd.concat(
        [
            tehran_summary,
            sanandaj_summary,
        ],
        ignore_index=True,
    )

    output_path = (
        OUTPUT_DIR / "city_temperature_summary.csv"
    )

    comparison.to_csv(
        output_path,
        index=False,
    )

    print("\nCity Temperature Comparison:")
    print(comparison)

    print(
        f"\nSaved to: {output_path}"
    )


if __name__ == "__main__":
    main()