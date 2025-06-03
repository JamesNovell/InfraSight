Import pandas as pd

df["WearRate"] = df["BNR_Total"] / ((pd.to_datetime("today") - pd.to_datetime(df["First EOD Date"])).dt.days + 1)
df.to_csv("data/processed_unit_odometer_sample.csv", index=False)