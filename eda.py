import pandas as pd

# Load Dataset
df = pd.read_csv("unemployment.csv")

# -----------------------------
# BASIC INSPECTION
# -----------------------------

print("First 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)

# -----------------------------
# DATA CLEANING
# -----------------------------

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\nCleaned Column Names:")
print(df.columns)

# Convert Date column to datetime format
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True
)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove rows containing missing values
df = df.dropna()

# Verify cleaning
print("\nDataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())