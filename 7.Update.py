import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()

#   -------------- UPDATE   ----------------    #

mycursor.execute("UPDATE student SET Name='David' WHERE ID = 1")

## final step to tell the database that we have changed the table data
db.commit()