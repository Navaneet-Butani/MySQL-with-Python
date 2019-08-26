# To perform JOIN follow below steps:
#1. First you have to create another table here it is 'college' to do this execute 1st part and remain comment to the 2nd part.
#2. After creating table let's perform JOIN operation to do this commenting out 1st part and uncomment the 2nd part and execute individual JOIN from INNER, LEFT or RIGHT which one you want


import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user = "root",
    password = "",
    database = "studentdb"
)

mycursor = db.cursor()


#------------- Part-1 ----------------#

# Creating another table 'college' for joining it with the 'student' table
mycursor.execute("create table college(College_city varchar(30), College_name varchar(20))")

# Inserting into the table
mycursor.execute("INSERT INTO college(College_city, College_name) VALUES ('Perth', 'Perth International College')")
mycursor.execute("INSERT INTO college(College_city, College_name) VALUES ('Mumbai', 'IIT Bombay')")
mycursor.execute("INSERT INTO college(College_city, College_name) VALUES ('Landon', 'The Great London Arts College')")
mycursor.execute("INSERT INTO college(College_city, College_name) VALUES ('Ahmedabad', 'GEC')")

# Save the changes
db.commit()




# #------------- Part-2 -----------------#

# # We combine 'student' and 'college' tables with the "students's 'City'" field and "college's 'College_city'" field 

# # Perform only one at a time from the INNER, LEFT and RIGHT JOIN.
# #------ INNER JOIN ------#
# # INNER JOIN only shows the records where there is a match.
# mycursor.execute("SELECT student.Name, college.College_name FROM student INNER JOIN college ON student.City=college.College_city")


# #------- LEFT JOIN -------#
# # LEFT JOIN shows matches records as well as all other records of of LEFT TABLE(Here it is 'student'), and place 'None' as value which are not matched
# #mycursor.execute("SELECT student.Name, college.College_name FROM student LEFT JOIN college ON student.City=college.College_city")


# #-------- RIGHT JOIN ---------#
# # LEFT JOIN shows matches records as well as all other records of of RIGHT TABLE(Here it is 'college'), and place 'None' as value which are not matched
# #mycursor.execute("SELECT student.Name, college.College_name FROM student RIGHT JOIN college ON student.City=college.College_city")



# #--------- FOR 2nd Part ALL THE JOINS -------------#
# records = mycursor.fetchall()

# for i in records:
#     print(i)

