import pandas as pd

# Load dataset
df = pd.read_csv("../data/customer_churn.csv")

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(
    df['TotalCharges'],
    errors='coerce'
)

# Fill missing values
df['TotalCharges'].fillna(
    df['TotalCharges'].median(),
    inplace=True
)

# Total customers
print("Total Customers:", len(df))

# Churn distribution
print(df['Churn'].value_counts())

# Average Monthly Charges
print("Average Monthly Charges:",
      df['MonthlyCharges'].mean())

print("Data Cleaning Completed!")

# Export cleaned dataset
df.to_csv(
    "../output/cleaned_churn_data.csv",
    index=False
)

print("Cleaned dataset exported successfully!")