# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

# FIRST ALTERNATIVE IN CONNECTING AND QUERYING A DATABASE
# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print('USING VARIABLE con:\n')
print(df.head())

# SECOND ALTERNATIVE IN CONNECTING AND QUERYING A DATABASE
# Open engine connection: con
with engine.connect() as con:

# Perform query: rs
    rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
    df = pd.DataFrame(rs.fetchall())

# Print head of DataFrame df
print('\nUSING with:\n')
print(df.head())
