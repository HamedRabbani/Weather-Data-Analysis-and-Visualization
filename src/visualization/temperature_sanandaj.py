from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = (
    BASE_DIR
    / "data"
    / "processed"
    / "sanandaj.csv"
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

    df = pd.read_csv(DATA_PATH)

    df["DATE"] = pd.to_datetime(df["DATE"])

    plt.figure(figsize=(12, 6))

    plt.plot(
        df["DATE"],
        df["TMAX_C"],
        label="Maximum Temperature",
        linewidth=2,
    )

    plt.plot(
        df["DATE"],
        df["TMIN_C"],
        label="Minimum Temperature",
        linewidth=2,
    )

    plt.title(
        "Daily Maximum and Minimum Temperature - Sanandaj"
    )

    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    output_path = (
        OUTPUT_DIR
        / "temperature_high_low_sanandaj.png"
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