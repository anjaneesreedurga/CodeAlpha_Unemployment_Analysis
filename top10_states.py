import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("unemployment.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Average unemployment by state
state_data = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

# Top 10 states
top10 = state_data.sort_values(ascending=False).head(10)

print(top10)

# Plot
plt.figure(figsize=(10,6))
top10.plot(kind="barh")

plt.title("Top 10 States by Average Unemployment Rate")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")

plt.tight_layout()
plt.show()