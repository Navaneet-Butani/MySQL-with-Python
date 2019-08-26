# Select only one in a while(Execute only one part which is required)

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()

#You can limit the number of records returned from the query, by using the "LIMIT" statement
mycursor.execute("SELECT * FROM student LIMIT 5")


#If you want to return five records, starting from the third record, you can use the "OFFSET" keyword
#mycursor.execute("SELECT * FROM student LIMIT 5 OFFSET 2")



myresult = mycursor.fetchall()

for x in myresult:
  print(x)