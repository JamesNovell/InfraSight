import pandas as pd
from datetime import datetime

df = pd.read_csv("../data/processed_sample.csv")
df["Days Active"] = (datetime.today() - pd.to_datetime(df["First EOD Date"])).dt.days
df["Wear Rate"] = df["BNR_Total"] / (df["Days Active"] + 1)
df["Maintenance Flag"] = df["BNR_Total"] > 2500000  # example threshold

df.to_csv("../data/final_metrics.csv", index=False)
print("Data cleaned and metrics calculated.")