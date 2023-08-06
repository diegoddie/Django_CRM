import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'diego',
    passwd = 'password123'
)

cursorObject = db.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done")