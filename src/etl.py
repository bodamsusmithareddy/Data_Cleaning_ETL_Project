
import pandas as pd
from sqlalchemy import create_engine

# Load raw CSV
df = pd.read_csv("data/raw_customers.csv")

print(" Raw data preview:")
print(df)

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

print("\n Cleaned data preview:")
print(df)

# Load into Postgres
# Update this connection string to match your setup
engine = create_engine("postgresql://postgres:password@localhost:5432/de_project")

# Insert data
df.to_sql("customers", con=engine, if_exists="append", index=False)

print("\n ETL pipeline completed and data loaded into Postgres!")
