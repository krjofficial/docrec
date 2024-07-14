import mysql.connector  # or psycopg2 for PostgreSQL

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE DocRecDB")
print("Database Created")