import sqlite3

username = input("Enter username: ")
query = "SELECT * FROM users WHERE name = '" + username + "'"
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(query)
