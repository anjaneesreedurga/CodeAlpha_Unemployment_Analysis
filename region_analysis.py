import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("unemployment.csv")

# Remove extra spaces
df.columns = df.columns.str.strip()

region_data = df.groupby("Area")[
    "Estimated Unemployment Rate (%)"
].mean()

print(region_data)

region_data.plot(kind="bar")

plt.title("Average Unemployment Rate by Area")
plt.xlabel("Area")
plt.ylabel("Unemployment Rate (%)")

plt.show()