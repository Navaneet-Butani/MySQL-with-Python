
# To implement python with MySQL Database and to use mysql.connector follow below steps:
# Install mysql.connector connector for Mysql database with the use of pip (python -m pip install mysql-connector)
# 1. Open Xampp Server
# 2. Start MySQL and Apache
# 3. Coonect to the "http://localhost/phpmyadmin" from the browser
# 4. Then execute your code for MySQL Database 

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",      #Username of user
  passwd=""     #password of user of above username
)


#To print database object
#print(mydb)

# creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
mycursor = mydb.cursor()

# below statement is used to create tha 'MySQLDemoDB' database
mycursor.execute("CREATE DATABASE StudentDB")

#executing the statement using 'execute()' method
mycursor.execute("SHOW DATABASES")

# 'fetchall()' method fetches all the rows from the last executed statement
databases = mycursor.fetchall()     # it returns a list of all databases present

# To print all the databases
print(databases)

## showing one by one database
for database in databases:
    print(database)


