import pandas as pd

# Load dataset
df = pd.read_csv("unemployment.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove missing values
df = df.dropna()

# Average unemployment rate by state
state_unemployment = df.groupby("Region")[
    "Estimated Unemployment Rate (%)"
].mean()

# Sort from highest to lowest
state_unemployment = state_unemployment.sort_values(
    ascending=False
)

print(state_unemployment)