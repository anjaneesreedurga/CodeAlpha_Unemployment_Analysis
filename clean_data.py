import pandas as pd

# Load dataset
df = pd.read_csv("unemployment.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True
)

# Check missing values before cleaning
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())