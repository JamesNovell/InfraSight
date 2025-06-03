import pandas as pd

df = pd.read_csv("data/unit_odometer_sample.csv")
print(df.describe())