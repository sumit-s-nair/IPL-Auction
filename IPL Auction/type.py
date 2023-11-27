import mysql.connector

cnx=mysql.connector.connect(host='127.0.0.1',
            database='iplplayers',
            user='root',
            password='admin')

cur=cnx.cursor()
cur.execute("select * from auction;")
l=cur.fetchone()
