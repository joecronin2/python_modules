import os
from typing import Tuple

missing = []

try:
    import numpy as np
except ModuleNotFoundError:
    missing.append("numpy")

try:
    import pandas as pd
except ModuleNotFoundError:
    missing.append("pandas")

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    missing.append("matplotlib")

if missing:
    print("Missing dependencies:", ", ".join(missing))
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
    return pd.DataFrame({"time": x, "signal": y})


def plot_data(df: pd.DataFrame) -> None:
    plt.figure()
    plt.plot(df["time"], df["signal"])
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time")
    plt.ylabel("Signal")
    plt.savefig("matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    import numpy
    import pandas
    import matplotlib

    print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    print(f"[OK] numpy ({numpy.__version__}) - Numerical computation ready")
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")

    x, y = generate_data(1000)
    df = analyze_data(x, y)
    plot_data(df)

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
