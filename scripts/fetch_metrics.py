import pandas as pd
import os

def main():
    input_path = "data/unit_odometer_sample.csv"

    # Check if the file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    print(f"Loading sample data from: {input_path}")
    df = pd.read_csv(input_path)

    # Basic validation
    required_cols = ["Serial Number", "BNR_Total", "First EOD Date"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing expected column: {col}")

    # Print summary
    print("Dataset Summary:")
    print(df.describe())

    # Optional: Save cleaned or renamed output
    output_path = "data/processed_sample.csv"
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to: {output_path}")

if __name__ == "__main__":
    main()
