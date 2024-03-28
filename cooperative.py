
import mysql.connector as sql

# mycon = sql.connect(host='localhost', user='root', password='aliyu090')
# print(mycon)
# mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE cooperative_society")
# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#     print(db)
   

mycon = sql.connect(host='localhost', user='root', passwd='aliyu090', database="cooperative_society")
mycursor = mycon.cursor()

# mycursor.execute("CREATE TABLE Register_table1 (customer_id INT(4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR(50), Email VARCHAR(50), Gender VARCHAR(20), Date_birth VARCHAR(50), Occupation VARCHAR(50), Date VARCHAR(40), Contact VARCHAR(11))")
# mycursor.execute("CREATE TABLE Saving_table2(customer_id int, Full_name VARCHAR(50), Contact VARCHAR(11), Account_no VARCHAR(11), Account_balance float, Interest float, Total float, Duration VARCHAR(30))")
# mycursor.execute("CREATE TABLE loan_table3(loan_id int(5) PRIMARY KEY AUTO_INCREMENT, customer_id int, Full_name VARCHAR(50), Duration VARCHAR(30), issue_date VARCHAR(30), loan_amount float, Interest float, Total float)")
# mycursor.execute("CREATE TABLE payback_loan_table4(loan-id int, Full_name VARCHAR(50), issue_date VARCHAR(30), loan_amount float, Interest float, Total float)")
# mycursor.execute("SHOW TABLES")
# for table in mycursor: 
#     print(table)
class cooperative:
    def __init__(self):
        print('''
              Welcome to credit cooperative society
              
               Please choose the option below...
            
                1. Register_member
                2. Saving
                3. Loan
                4. Payback_loan
                5. Member_details
                6. Quit
            
             ''')
        choice = input("Enter your choice:")
        if choice == '1':
            self.Register_member()
        elif choice == '2':
            self.Saving()
        elif choice == '3':
            self.Loan()
        elif choice == '4':
            self.Payback_loan()
        elif choice == '5':
            self.Member_details()
        elif choice == '6':
            self.Quit()
            
    def Register_member(self):
        print("Register>>>") 
        Full_name = input("Enter your fullname:") 
        Email = input("Enter your valid email:")
        Gender = input("Your Gender:")
        Date_birth = input("Your date of birth:")
        Occupation = input("Enter your occupation:")
        Date = input("Enter date join:")
        contact = input("Enter valid contact:")
        query1 = 'INSERT INTO register_table1(Full_name,Email,Gender,Date_birth,Occupation,Date,contact) VALUE(%s, %s, %s, %s, %s, %s, %s)'
        val1 = (Full_name,Email,Gender,Date_birth,Occupation,Date,contact)
        mycursor.execute(query1,val1)
        mycon.commit()
        print(mycursor.rowcount, 'row added')
        
    def Saving(self):
        customer_id=input('Enter your ID:')
        Full_name=input('Enter your register name:')
        Contact=input("Enter your valid contact:")
        Account_no=input("Enter your account no:")
        Account_balance=input("Enter amount to save:")
        Interest=input("10 percent monthly:")
        Total=input("Enter total amount:")
        Duration=input("Enter duration:")
        query2 = 'INSERT INTO Saving_table2(customer_id,Full_name,Contact,Account_no,Account_balance,Interest,Total,Duration) VALUE(%s, %s, %s, %s, %s, %s, %s, %s)'
        val2 = (customer_id,Full_name,Contact,Account_no,Account_balance,Interest,Total,Duration)
        mycursor.execute(query2,val2)
        mycon.commit()
        print(mycursor.rowcount, 'row added')

    def Loan(self):
        print("Fill the form below..")
        customer_id = input("Enter your member_id")
        Full_name=input("Enter your name:")
        Duration=input("Enter duration:")
        issue_date = input("Enter issue date:")   
        loan_amount=float(input("Enter amount:"))
        Interest=float(input('20 percent monthly:'))
        Total=float(input("Enter total amount:"))

        query3 = "INSERT INTO loan_table3 (customer_id,Full_name,Duration,issue_date,loan_amount,Interest,Total) VALUE(%s,%s,%s,%s,%s,%s,%s)"
        val3 = (customer_id,Full_name,Duration,issue_date,loan_amount,Interest,Total)
        mycursor.execute(query3,val3)
        mycon.commit()
        print(mycursor.rowcount, 'row added')
    def Payback_loan(self):
        loan_id = int(input("Enter your loan_id>>"))
        Full_name = input("Enter name:")
        issue_date = input("Enter date you collect loan:") 
        loan_amount = input("Enter the loan amount:") 
        Interest= input("20 percenr monthly:")
        Total=input('Enter total money return:')  
        query4 = "INSERT INTO payback_loan_table4 (loan_id,Full_name,issue_date,loan_amount,Interest,Total) VALUE(%s,%s,%s,%s,%s,%s)"
        val4 = (loan_id,Full_name,issue_date,loan_amount,Interest,Total)
        mycursor.execute(query4,val4)
        mycon.commit()
        print(mycursor.rowcount, 'row added')
        
      
    def Member_details(self):
        print('''
            Please enter option below
            
            1. member_profile
            2. saving
            3. loan_history
            ''')  
        choice = input("Enter your choice:")
        if choice == '1':
            self.member_profile() 
        elif choice == '2':
            self.saving()
        elif choice == '3':
            self.loan_history()  
    def saving(self):
        Account_no = input("Enter your account_no:")
        a = 'SELECT * FROM Saving_table2 WHERE Account_no=%s'
        data = [Account_no]
        mycursor.execute(a, data)
        result = mycursor.fetchall()
        print(result)
        mycon.commit()  
        
    def loan_history(self): 
        Full_name = input("Enter your Full_name:")
        a2 = 'SELECT * FROM loan_table3 WHERE Full_name=%s'
        data2 = [Full_name]
        mycursor.execute(a2, data2)
        result = mycursor.fetchall()
        print(result)
        mycon.commit() 
        
    def member_profile(self):
        Full_name = input("Enter your Full_name:")
        a3 = "SELECT * FROM register_table1 WHERE Full_name=%s"
        data3 = [Full_name]
        mycursor.execute(a3, data3)
        result = mycursor.fetchall()
        print(result)
        mycon.commit()    
    
    def Quit(self):
        print("is Cancel..")                     
                          
credit=cooperative()        
   
    
    
    