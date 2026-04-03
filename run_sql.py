import sqlite3

conn = sqlite3.connect('Telco_Analysis.db')
cursor = conn.cursor()

# Read the logic from your external SQL file
with open('transformations.sql', 'r') as f:
    sql_logic = f.read()

try:
    cursor.executescript(sql_logic)
    conn.commit()
    print("Star Schema deployed from transformations.sql!")
except Exception as e:
    print(f"❌ Error: {e}")
finally:
    conn.close()