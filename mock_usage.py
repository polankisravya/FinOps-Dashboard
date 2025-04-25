
import sqlite3
import datetime
import random

# Connect to local SQLite database
conn = sqlite3.connect('usage.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS usage (
    date TEXT,
    amount REAL,
    service TEXT
)
''')

# Services to simulate
services = ['Compute Engine', 'Cloud Storage', 'Cloud Functions']
today = datetime.date.today()

# Insert 10 days of random mock data
for i in range(10):
    for service in services:
        date = today - datetime.timedelta(days=i)
        amount = round(random.uniform(0.2, 3.0), 2)
        cursor.execute("INSERT INTO usage (date, amount, service) VALUES (?, ?, ?)",
                       (str(date), amount, service))

conn.commit()
print("Mock usage data inserted.")
