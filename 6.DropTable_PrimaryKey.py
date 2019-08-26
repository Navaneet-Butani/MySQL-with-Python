# Select only one in a while(Execute only one part which is required)

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()

# first we have to 'drop' the table which has already created to create it again with the 'PRIMARY KEY'
## 'DROP TABLE table_name' statement will drop the table from a database
mycursor.execute("DROP TABLE student")


# creating the 'users' table again with the 'PRIMARY KEY'
#mycursor.execute("CREATE TABLE student(ID INT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, Name varchar(20), City varchar(30))")


# adding 'id' column to the 'student' table
## 'FIRST' keyword in the statement will add a column in the starting of the table
#mycursor.execute("ALTER TABLE student ADD COLUMN ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")


#'DESC table_name' is used to get all columns information
#mycursor.execute("DESC student")

# it will print all the columns as 'tuples' in a list
print(mycursor.fetchall())