import sqlite3

connection =sqlite3.connection("student.db")

curs = connection.cursor()

firstname = input("Enter your firstname: ")
lastname = input("Eter your lastname: ")


#this create a database table
sqlCreate = "CREATE TABLE records (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,firstname TEXT, lastname TEXT)"

#THIS QUERRY INSERT DATA TO THE DATABASE TABLE
sqlInsert = "INSERT INTO recorrds(id, firstname,lastname)VALUES(NULL,'%s','%s')"%(firstname,lastname)

#this querry will retrieve data from the database
sqlRetrieve= "SELECT * FROM records"

#Removing a data in database
sqlRemove = "DELETE FROM records WHERE id = %d "% idNumber


newFirstname = input("Enter your name firstname: ")
newLastname = input("Enter your lastname: ")
ids = int(input("Enter the user id to update: "))

#updating a data in database
sqlUpdate = "UPDATE records SET(firstname, lastname) = ('%s','%s') WHERE id = %d " %(newFirstname,newLastname,ids)

#this create a database table
try:
    curs.execute(sqlCreate)
except Exception as s:
    print(s)

curs.execute(sqlInsert)
print("Data inserted Successful")


#this remove a data from the database
curs.execute(sqlRemove)

#this code update a single data in the database using its id number
curs.execute(sqlUpdate)
print("data updated successful! ")


#to retrieve data in database , using fetchhall() or fetchone(one) or fecthmany(numbers of items)
curs.execute(sqlRetrieve)
print(curs.fetchall())

connection.commit()

curs.close()

















