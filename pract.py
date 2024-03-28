import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='aliyu090', database="Bank")


def openaccount():
    name = input("Enter the name:")
    account_no = input("Enter account_no")
    dat = input("Enter the date of bith")
    add = input("Enter the add:")
    contact = input("Enter the contact:")
    open = int(input("Enter the amount:"))
    
    data1 =(name,account_no,dat,add,contact,open)
    data2 =(name,account_no,open)
    sql1=("insert into account_table values (%s, %s, %s, %s, %s, %s)")
    sql2=("insert into amount_table values (%s, %s, %s)")
    x = mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Enter successfully..")
    main()
    
def deposit():
    amount =input("Enter the amount:")
    account_no = input ("Enter the account_no:")
    a = "select * from amount where account_no accNo=%s"  
    data =(account_no)  
    x = mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    t=result[0]+amount
    sql= ("update amount_table set balance where account_no = %s")
    d = (t,account_no)
    x.execute(sql,d)
    mydb.commit()
    main()
def withdraw(): 
    amount =input("Enter the amount:")
    account_no = input ("Enter the account_no:")
    a = "select balance from amount_table where account_no=%s"  
    data =(account_no)  
    x = mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    t=result[0] - amount
    sql= ("update amount_table set balance where account_no = %s")
    d = (t,account_no)
    x.execute(sql,d)
    mydb.commit()
    main()  
def balance():
    account_no = input ("Enter the account_no:")
    a = "select from amount_table where account_no=%s" 
    data=(account_no)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    print("Balance for account:",account_no,"is", result[-1])
    main()
    
def details():
    account_no = input ("Enter the account_no:")
    a = "select from amount_table where account_no accNo=%s" 
    data=(account_no)
    x=mydb.cursor()
    x.execute(a, data)
    result=x.fetchone()
    for i in result:
        print(i)  
        
def closeaccount():
    account_no = input("Enter the account no:")
    sql1="delete from account_table where accNo =%s"
    sql2="delete from amount_table where  accno=%s"
    data=(account_no)
    x=mydb.cursor()
    x.execute(sql1,data)
    x.execute(sql2, data)
    mydb.commit()
    main
    
    

def main():
    print('''
      1. openaccount
      2. deposit 
      3. withdraw
      4. balance
      5. details
      6. closeaccount
      ''')
    choice = input("Enter your choice:")
    if choice == ('1'):
        openaccount()
    elif choice == ('2'):
        deposit()
    elif choice == ('3'):
        withdraw()
    elif choice == ('4'):
        balance()
    elif choice == ('5'):
        details()
    elif choice == ('6'):
        closeaccount()
main()