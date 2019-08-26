# Select only one in a while(Execute only one part which is required)

import mysql.connector as sql

db = sql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()



# Insert single row

# Query for inserting rows in table
mycursor.execute("INSERT INTO student (ID, Name, City ) VALUES (1, 'Kevin', 'Perth')")
mycursor.execute("INSERT INTO student (ID, Name, City ) VALUES (2, 'Raj', 'Mumbai')")
mycursor.execute("INSERT INTO student (ID, Name, City ) VALUES (3, 'Shane', 'Dubai')")
mycursor.execute("INSERT INTO student (Id, Name, City ) VALUES (4, 'Shaun', 'Sidney')")





# # Instert multiple rows

# query = "INSERT INTO student (ID, Name, City) VALUES (%s, %s, %s)"

# values = [
#     (11, "Mitesh", "Gandhinagar"),
#     (12, "Andrew", "Landon"),
#     (13, "Rickey", "Melborne")
# ]

# mycursor.executemany(query, values)




# to make final output we have to run the 'commit()' method of the database object
db.commit()

print(mycursor.rowcount, " row inserted!")