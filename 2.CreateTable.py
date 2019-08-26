import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()

# creating a table called 'student' in the 'studentdb' database
mycursor.execute("create table student(ID Integer(5), Name varchar(20), City varchar(30))")

# getting all the tables which are present in 'studentdb' database
mycursor.execute("SHOW TABLES")

table = mycursor.fetchall()     # it returns list of tables present in the database

print(table)        # it prints all the tables into the database into the list

