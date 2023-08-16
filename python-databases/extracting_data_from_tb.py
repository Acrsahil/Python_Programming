import mysql.connector as connects
mydb = connects.connect(
    host = 'localhost',
    user = 'root',
    password = 'dassahil123',
    database = 'db1'
) # it is mandatory

cur = mydb.cursor() #creting curser
s = "Select * from book"
cur.execute(s) #executing the query
result = cur.fetchall() #result are in tuple 
for rec in result: # printing each tuple in itrative method
    print(rec)
