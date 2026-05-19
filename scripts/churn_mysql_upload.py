import pandas as pd
from sqlalchemy import create_engine

# Load cleaned dataset
df = pd.read_csv(
    "../output/cleaned_churn_data.csv"
)

# MySQL credentials
username = "root"
password = "Ayush%402003"
host = "localhost"
database = "customer_churn_project"

# Create MySQL connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Upload dataset into MySQL
df.to_sql(
    name="customer_churn",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customer churn data uploaded successfully!")