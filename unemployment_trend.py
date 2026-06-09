import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove missing values
df = df.dropna()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Average unemployment rate by date
trend = df.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean()

# Plot
plt.figure(figsize=(12,6))

plt.plot(trend.index, trend.values)

plt.title("Average Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)

plt.tight_layout()
plt.show()