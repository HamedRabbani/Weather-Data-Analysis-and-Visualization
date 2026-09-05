from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)

OUTPUT_DIR = (
    BASE_DIR
    / "outputs"
    / "figures"
)

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


def main():

    tehran = pd.read_csv(
        PROCESSED_DIR / "tehran.csv"
    )

    sanandaj = pd.read_csv(
        PROCESSED_DIR / "sanandaj.csv"
    )

    tehran["DATE"] = pd.to_datetime(
        tehran["DATE"]
    )

    sanandaj["DATE"] = pd.to_datetime(
        sanandaj["DATE"]
    )

    plt.figure(figsize=(12, 6))

    plt.plot(
        tehran["DATE"],
        tehran["TMAX_C"],
        label="Tehran",
        linewidth=2,
    )

    plt.plot(
        sanandaj["DATE"],
        sanandaj["TMAX_C"],
        label="Sanandaj",
        linewidth=2,
    )

    plt.title(
        "Daily Maximum Temperature Comparison"
    )

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    output_path = (
        OUTPUT_DIR
        / "comparing_two_cities.png"
    )

    plt.savefig(
        output_path,
        dpi=150,
        bbox_inches="tight",
    )

    plt.show()

    print(f"Figure saved to: {output_path}")


if __name__ == "__main__":
    main()