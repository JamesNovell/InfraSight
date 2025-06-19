import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data():
    path = "../data/final_metrics.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed data not found: {path}")
    return pd.read_csv(path)

def plot_top_units(df):
    top_units = df.sort_values("BNR_Total", ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    plt.barh(top_units["Serial Number"], top_units["BNR_Total"], color="skyblue")
    plt.xlabel("Total Cycles (BNR_Total)")
    plt.title("Top 10 Units by Usage")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig("../docs/top_units_usage.png")
    print("📊 Saved chart: docs/top_units_usage.png")

def plot_avg_wear_by_state(df):
    grouped = df.groupby("State")["Wear Rate"].mean().sort_values(ascending=False)
    plt.figure(figsize=(12, 6))
    grouped.plot(kind="bar", color="coral")
    plt.ylabel("Average Wear Rate")
    plt.title("Average Wear Rate by State")
    plt.tight_layout()
    plt.savefig("../docs/avg_wear_by_state.png")
    print("📊 Saved chart: docs/avg_wear_by_state.png")

def main():
    df = load_data()
    plot_top_units(df)
    plot_avg_wear_by_state(df)

if __name__ == "__main__":
    main()
