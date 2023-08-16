import mysql.connector as connects
mydb = connects.connect(host = 'localhost',
                        user='root',
                        password='dassahil123',
                        database = 'db1')
cur = mydb.cursor()
s = "INSERT INTO book values (%s,%s,%s)"
books = [(4,'Php',136),(3,'Java8',450),(4,'HTML',490),]
cur.executemany(s,books)
mydb.commit()