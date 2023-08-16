import mysql.connector as connects
mydb = connects.connect(host = 'localhost',
                        user='root',
                        password='dassahil123',
                        database = 'db1')
cur = mydb.cursor()
s = "INSERT INTO book values (%s,%s,%s)"
bookid = int(input("Enter the book id: "))
title = input("Enter the name of book: ")
price = float(input("Enter the price of book: "))
b1 = (bookid,title,price)
cur.execute(s,b1)
mydb.commit()