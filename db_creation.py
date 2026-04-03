import pandas as pd
import sqlite3

# 1. Load the CSV you downloaded
df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

# 2. Quick Clean (Fixing the TotalCharges space issue)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)

# 3. Create a connection to a local SQL database
conn = sqlite3.connect('Telco_Analysis.db')

# 4. Load the raw data into a "Staging" table
df.to_sql('stg_telco_data', conn, if_exists='replace', index=False)

print("Success! Your SQL Database 'Telco_Analysis.db' has been created.")
conn.close()