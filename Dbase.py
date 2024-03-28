
# Python Database (Mysql)
# To download mysql connector user: pip install mysql-connector if you use xamp
# or
# pip install mysql-connector-python if you use MySQL workbench

import mysql.connector as sql


mycon = sql.connect(host='localhost', user='root', password='aliyu090')
# print(mycon)
mycursor = mycon.cursor()

mycursor.execute("SHOW DATABASES")
print(mycursor)
for db in mycursor:
    print(db)

# mycursor.execute("CREATE DATABASE atm_db")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)

# mycon = sql.connect(host='localhost', user='root', passwd='aliyu090', database="atm_db")
# mycursor = mycon.cursor()

# mycursor.execute("CREATE TABLE customers_table (ctm_id INT(4), Full_Name VARCHAR(40), Address VARCHAR(50), Phone VARCHAR(11), Username VARCHAR(20), Password VARCHAR(20))")

# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)

# mycursor.execute("ALTER TABLE customers_table CHANGE ctm_id customer_id INT(5) PRIMARY KEY AUTO_INCREMENT")
# mycursor.execute("ALTER TABLE customers_table ADD UNIQUE(Phone);")
# mycursor.execute("ALTER TABLE customers_table ADD UNIQUE(Username);")

# myquery = "INSERT INTO customers table (Full_Name, Address, Phone, Username, Password) VALUES(%s, %s, %s, %s, %s)"
# val = ('Timi Adesola', 'Owolake', '07162305688', 'Timi', '1234')
# mycursor.execute(myquery, val)
# mycon.commit()
# mycon.close()

# fulname = input('enter your full name >') 
# address = input('enter your address ')
# phone = input('enter your phone number ')
# user = input('enter your username ')
# password = input('enter your Password ')

# myquery = "INSERT INTO customers table (Full_Name, Address, Phone, Username, Password) VALUES(%s, %s, %s, %s, %s)"
# val = (fulname, address, phone, user, password)
# mycursor.execute(myquery, val)
# mycon.commit()
# print(mycursor.rowcount, "records submitted successfully")
# mycon.close()

# myquery = "INSERT INTO customers_table (Full_Name, Address, Phone, Username, Password) VALUES(%s, %s, %s, %s, %s)"
# val = [("Timi Ade", "General", "09048584322", "tyt", "1122"), ("Adeola John", "General", "08094993322", "john", "1232")]
# mycursor.executemany(myquery, val)
# mycon.commit()
# print(mycursor.rowcount, "records inserted successfully")
# mycon.close()
# # # 
# query = "SELECT * FROM customer_table"
# mycursor.execute(query)
# output = mycursor.fetchall()
# print(output)
# # for info in output:
# #   print(info)

# output = mycursor.fetchone()
# print(output)

# query = "SELECT * FROM customers_table WHERE Address=%s"
# val = ('ajoke',)
# mycursor.execute(query, val)
# myreg = mycursor.fetchall()
# myreg = mycursor.fetchone()
# print(myreg)