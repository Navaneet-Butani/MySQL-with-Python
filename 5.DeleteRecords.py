import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()


# ------------  DELETE  --------------- #
# Delete specific records with 'WHERE' clause
mycursor.execute("DELETE FROM student WHERE ID=3")


# final step to tell the database that we have changed the table data
db.commit()


print(mycursor.rowcount, "record(s) deleted")