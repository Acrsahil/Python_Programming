import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'dassahil123',
    database = 'db1'
)
cur = mydb.cursor()
s = "delete from book where title = 'Php'"
cur.execute(s)
mydb.commit()