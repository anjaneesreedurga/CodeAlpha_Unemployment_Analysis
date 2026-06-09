import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean columns
df.columns = df.columns.str.strip()

# Remove missing values
df = df.dropna()

# Average unemployment by state
state_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

# Top 10 states
top10 = state_unemployment.sort_values(
    ascending=False
).head(10)

# Plot
plt.figure(figsize=(10,6))

top10.plot(kind="bar")

plt.title("Top 10 States by Average Unemployment Rate")
plt.xlabel("State")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()