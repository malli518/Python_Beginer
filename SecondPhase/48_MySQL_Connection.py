import mysql.connector
con = mysql.connector.connect(host='localhost', port=3306, user='root', passwd='root', db='test')
cur = con.cursor()
cur.execute("select * from test.employeeinfo;")

print(cur.description)
result = cur.fetchone()
for i in result:
    print(i)
print()

for row in cur:
    print(row)

cur.close()
con.close()
