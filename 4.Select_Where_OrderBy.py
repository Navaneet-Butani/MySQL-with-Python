# Select only one in a while(Execute only one part which is required)

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()

#   ----------  SELECT ------------   #

# getting ALL records from the table
mycursor.execute("SELECT * FROM student")


## getting 'Name' column from the table
#mycursor.execute("SELECT Name FROM student")




#   ---------   WHERE STATEMENT    ------------ #

## getting records with specific conditions with "WHERE"
#mycursor.execute("SELECT * FROM student WHERE ID = 2")





#   -----------     ORDER BY    ----------------    #

## Sorting the data in ascending order using the name column
#mycursor.execute("SELECT * FROM student ORDER BY name")

## Sorting the data in descending order by name column
#mycursor.execute("SELECT * FROM student ORDER BY name DESC")





records = mycursor.fetchall()

for i in records:
    print(i)

