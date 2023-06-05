from sqlalchemy import create_engine

# Create an engine and connect to a SQLite database
engine = create_engine('sqlite:///mydatabase.db')

# Create a connection
connection = engine.connect()

# Perform database operations
result = connection.execute("SELECT * FROM mytable")
for row in result:
    print(row)

# Close the connection
connection.close()
