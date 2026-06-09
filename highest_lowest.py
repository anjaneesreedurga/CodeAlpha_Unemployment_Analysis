import pandas as pd

df = pd.read_csv("unemployment.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

highest = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean().sort_values(ascending=False)

print("Top 5 Highest Unemployment States:")
print(highest.head())

print("\nTop 5 Lowest Unemployment States:")
print(highest.tail())