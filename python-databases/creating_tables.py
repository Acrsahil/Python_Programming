import mysql.connector as connects
mydb = connects.connect(host = 'localhost',
                        user='root',
                        password='dassahil123',
                        database='db1')
cur=mydb.cursor()
s = "CREATE TABLE book(bookid int(4),title varchar(20),price float(5,2))"
cur.execute(s)

