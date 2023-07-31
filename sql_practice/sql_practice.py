"""
this python module performs the basic operations in sql
"""
import sqlite3

## 1) Establish a connection
con = sqlite3.connect('database.db')
## 2) Create a cursor for queries
cur = con.cursor()

### 3) Create queries in SQL
cur.execute("SELECT * FROM 'ips' ORDER BY asn")
print(cur.fetchall())
print("-------------------------")

## GEt all rows and certain columns
cur.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cur.fetchall())
print("-------------------------")

## Extract just a portion of the rows: rows where asn is less than 300
cur.execute("SELECT address, asn FROM 'ips' WHERE asn < 300")
print(cur.fetchall())
print("-------------------------")

## Where asn is an especific value: 144
cur.execute("SELECT address, asn FROM 'ips' WHERE asn = 144")
print(cur.fetchall())
print("-------------------------")

### Multiple conditions
cur.execute("SELECT address, asn, domain FROM 'ips' WHERE asn<300 and domain LIKE '%sa' ")
results1 = cur.fetchall()
print(results1)
print("-------------------------")


for row in results1:
    print(row)
    
