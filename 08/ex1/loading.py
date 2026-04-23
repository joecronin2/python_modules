import sys
import os
from typing import Tuple

try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    print("numpy, pandas, or matplotlib missing...")
    exit(1)


def detect_environment() -> str:
    if "POETRY_ACTIVE" in os.environ:
        return "poetry"
    elif "VIRTUAL_ENV" in os.environ:
        return "venv/pip"
    return "system"


def generate_data(n: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
    x: np.ndarray = np.linspace(0, 10, n)
    y: np.ndarray = np.sin(x) + np.random.normal(0, 0.2, size=n)
    return x, y


def analyze_data(x: np.ndarray, y: np.ndarray) -> pd.DataFrame:
    df: pd.DataFrame = pd.DataFrame({"time": x, "signal": y})
    return df


def plot_data(df: pd.DataFrame) -> None:
    plt.figure()
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.savefig("matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    env: str = detect_environment()
    print(f"\nEnvironment: {env}")

    print("\nAnalyzing Matrix data...")
    x, y = generate_data(1000)

    print("Processing 1000 data points...")

    df: pd.DataFrame = analyze_data(x, y)

    print("\nData summary:")
    print(df.describe())

    print("\nGenerating visualization...")
    plot_data(df)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
