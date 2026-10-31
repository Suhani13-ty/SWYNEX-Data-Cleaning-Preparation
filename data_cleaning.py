import pandas as pd

# Load the original dataset
df = pd.read_csv("raw_data.csv")

# Standardize text fields
for col in ["Name", "City", "Email"]:
    df[col] = df[col].astype("string").str.strip()

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()
df["Email"] = df["Email"].str.lower()

# Convert numeric columns; invalid values become missing
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Purchase_Amount"] = (
    df["Purchase_Amount"].astype("string").str.replace(",", "", regex=False)
)
df["Purchase_Amount"] = pd.to_numeric(df["Purchase_Amount"], errors="coerce")

# Parse dates consistently
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce", dayfirst=True)

# Treat impossible ages and invalid/non-positive purchase amounts as missing
df.loc[~df["Age"].between(0, 100), "Age"] = pd.NA
df.loc[df["Purchase_Amount"] <= 0, "Purchase_Amount"] = pd.NA

# Remove duplicate customer records (keep first occurrence)
df = df.drop_duplicates(subset=["Customer_ID"], keep="first")

# Fill missing values with transparent, simple rules
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df["Email"] = df["Email"].fillna("Not Provided")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())

# Export cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Cleaning complete. Saved cleaned_data.csv")
print(df.info())
print(df.head())
