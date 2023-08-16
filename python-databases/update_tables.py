import mysql.connector as connects
mydb = connects.connect(host = 'localhost',
                        user='root',
                        password='dassahil123',
                        database='db1')
cur=mydb.cursor()
s = "UPDATE book SET price = price + 10 WHERE price>200"
cur.execute(s)
mydb.commit()