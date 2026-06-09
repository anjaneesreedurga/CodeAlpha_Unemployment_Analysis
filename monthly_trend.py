import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Monthly average unemployment
monthly_data = df.groupby("Date")[
    "Estimated Unemployment Rate (%)"
].mean()

print(monthly_data)

# Plot
plt.figure(figsize=(10,5))
plt.plot(monthly_data.index, monthly_data.values)

plt.title("Monthly Average Unemployment Rate")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.grid(True)

plt.show()