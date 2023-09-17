import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'admin123'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE Cindy')

print("All Done!")