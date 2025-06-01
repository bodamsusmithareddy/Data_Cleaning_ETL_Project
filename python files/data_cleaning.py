
import pandas as pd

# Load raw CSV
df = pd.read_csv("data/raw_customers.csv")
print("Raw Data:")
print(df.head())

# Clean the data
df["name"] = df["name"].str.strip()
df["email"] = df["email"].str.strip().str.lower()
df["country"] = df["country"].str.strip().str.title()

# Remove rows with missing name/email
df = df.dropna(subset=["name", "email"])

# Deduplicate
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("data/cleaned_customers.csv", index=False)

print("Cleaned Data:")
print(df.head())
