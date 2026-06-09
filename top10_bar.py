import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("unemployment.csv")

df.columns = df.columns.str.strip()

top10 = (
    df.groupby("Region")
    ["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print(top10)

plt.figure(figsize=(10,6))
top10.plot(kind="bar")

plt.title("Top 10 States with Highest Average Unemployment")
plt.xlabel("State")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()