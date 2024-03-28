
# Python Error Handling
# Two types of error in programming:
# .compile time error
# .run time error

# try and except, finally 
# for i in range(3):
#     try:
#         a =int(input("Enter your first number:"))
#         b =int(input("Enter your second number:"))
#         print(a/b)
#     except ValueError:
#         print('value can not be letter') 
#     except ZeroDivisionError:
#         print('Divisor can not be zero:.')  
#     else:
#         print('No erroh was raise')
#     finally:
#         print('The execution was successfully.')             

# def simpleCal():
#     for i in range(5):
#         a = int(input("enter quotient value"))
#         b = int(input("enter divisor value"))
#         print(a/b)

# simpleCal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print('Divisor can not be letter.')    
# ca=cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except:
#             print("divisor can not be zero")
           
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print("Your value must not be letter or decimal")
# cal()

# def cal():
#     for i in range(5):
#         try:
#             a = int(input("enter quotient value"))
#             b = int(input("enter divisor value"))
#             print(a/b)
#         except ZeroDivisionError:
#             print("divisor can not be zero")
#         except ValueError:
#             print("Your value must not be letter")
#         except:
#             pass
#         else: # execute if no error was raised
#             print("no error was raised")
#         finally: # execute either there is error or not
#             print("the execution was successful")

# cal()

# import re
# a = input("enter quotient value")
# b = input("enter divisor value")
# if re.search(r'[a-zA-Z]', a) or re.search(r'[a-zA-Z]', b):
#     raise TypeError("first value or second value cannot contain letters")
# else:
#     print(int(a)/int(b))
