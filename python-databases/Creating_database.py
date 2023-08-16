import mysql.connector as connects
mydb = connects.connect(host = 'localhost',user='root',password='dassahil123')
cur = mydb.cursor()
cur.execute("delete database db1")