# if 5 > 2:
#     print('Five is greater than two')
    
# else:
#     print("Five is less than two")    

# python comment
# comment are use to avoid execution of a code

# python variable
# x = 6
# y = ('Aliyu', 'maigida', 'jarmai')
# print(x)
# print(y)

# casting is done when you are trying to specify data type
# x = str(3)
# x = str(3 * 5) + ' Apple ' #concatenation
# y = int(3)
# z = float(3)
# print(x)

# Assign multiple variable name

# variable name are case_ sensitive
# variable doesn't start with int
# it can be alpha-numeric

# many values to multiple variable

# x , y, z = 'Orange', 'Apple', 'Cherry'
# x = y = z ="Apple"
# x, y, z = 'Banana'
# multiple line comment
"""
# x = 'Apple'
# y = 'Apple'
# z = 'Apple'
# """
# print(x)
# print(y)
# print(z)
# make sure the number of variable maches the number of values

# Output variabls
 
# x = 'Awesome'
# print('Python is ' + x)

# x, y, z = 'really', 'really', 'good'
# print("Python is" + x + " " + y + " " + z)

# for numbers
# x = 5
# y =4
# print(x + y)

# Global variables
# Global variable are variables created outside the function

# x = "Awesome"   # global

# def myfunc():
#     print('Python is ' + x)
    
# myfunc() 

# Local variable   
# def myfunc():
#     x = "Awesome"
#     print('Python is ' + x)
    
# myfunc() 

# x ="Awesome" #global
# def myfunc():
#     x = "fantastic" #local
#     print('Python is ' + x)
    
# myfunc()
# print('Python is ' + x)

# global keyword

# def myfunc():
#     global x
#     x = 'Fantastic'
    
# myfunc()
# print('Python is ' + x)  

# def myfunc():
#     global x  #global scope
#     # to be able access outside myfunc
#     x = "really good"
    
# myfunc()
# print("Python is " + x)

# def myfunc():
#     global x  #global scope
    # to be able access outside myfunc
    # x = "really good"
   
# print("Python is " + x)      # error because you are try to print inside myfunc, beacuse of the global
# myfunc()

# Data type
    
# Text type: str
# Numeric type: int, float, coplex
# Sequence type: list, tuple, range 
# Mapping type: dict
# Set type: set, fronzenset
# Bolean type: bool
# Binary type: bytes, bytearray, memoryview


# complex is a combination of int and str
# x = 1j
# print(type(x))

    
# # range type
# x = range(6)
# print(x)
# print(type(x))

# Dict type
# x={'name' : 'Ality', 'age' : 23}
# print(x)
# print(type(x))

# set type
# x = {'apple', 'banana', 'cherry'}
# print(x)
# print(type(x))

# frozenset
# x = frozenset({'apple', 'banana', 'cherry'})
# print(x)
# print(type(x))

# bool
# x = True
# x = False
# print(x)
# print(type(x))
# print(bool("Hello"))
# print(10 > 9)
# print(10 == 9)
# print(10 <9)
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")   
# else:
#     print("b is not greater than a") 
# class myclass():
#     def __len__(self):
#         return 0
    
# myobj = myclass() 
# print(bool(myobj))   
       

# byte type
# x = b"Hello"
# print(x)
# print(type(x))

# # bytearray type
# x = bytearray(5)
# print(x)
# print(type(x))

# memoryview type

# x = memoryview(bytes(5))
# print(x)
# print(type(x))       

# string type
# b =  'Hello, World'
# # print(b)
# print(b[2])

# Loop
# for x in 'banana':
#     print(x)

# len function 
# a = 'Hello, World'
# print(len(a)) 

# check string
# txt = "The best things in life are free!"
# # print("free" in txt)
# if 'free' in txt:
#     print("'free' is in the string " +  txt + "")

# txt = "The best things in life are free!"
# # print("expensive" not in txt)
# print("best" not in txt)


# txt = "the best in life are free!"
# if "expensive" not in txt:
#     print("No,  'expensive' is not present.")

# MEMBERSHIP OPERATOR
# e.g x is y
# x = ['Banan', 'Apple']
# print('Apple' in x)
# print("apple" not in ["Banana", "Apple"])
#  x is not y


# identity operator

# x = ["apple", 'banana']
# z = ['apple', 'banana']
# y = x
# print(x == y)
# print(x is z)

# Logical operators
# it is use for conditional statement
# x = 5
# print(x > 3 and x < 10)
# print(x > 3 or x > 10)
# print(x)

# print(not(True))
# print(not(not(True)))

# comparision operator

# x = 5
# y = 5
# print(x == y)
# print(x != y)
# print(x > y)
# print(x >= y)
# print(5 <= 5)

# python operator
# x = 15
# y = 2
# print(x + y)
# print(x / y)
# floor division round the remainder down
# print(x//y)

# Assignment operator
# x = 5
# x += 3
# print(x)

# x = 5
# x -= 3
# print(x)

# x = 5
# x *= 3
# print(x)

# x = 5
# x /= 3
# print(x)

# x = 17
# x %= 3
# print(x)

# x = 5
# x //= 3
# print(x)

# escape character
# txt = "Hello\nworld!"
# txt2 = "Hello\rworld!"
# print(txt)
# print(txt2)
# txt = "hello \bworld!"
# print(txt)
# txt = "hello \bworld!"
# print(txt)
# txt = "hello \tworld!"
# print(txt)
# txt = "hello \fworld!"
# print(txt)

# format Strings
# age = '36'
# txt = "My name is John, I am " + age
# print(txt)
# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# python concatenation
# a = "Hello "
# b = "World"
# c = a + b
# print(c)
# a = "Hello"
# b = "World"
# c = a+ " "+b
# print(c)

# modify strings
# a = "Hello, World!"
# print(a.upper())

# remove white space
# a = " Hello, Wolrd! "
# print(a.strip())
# print(a.strip().lower())

# a = "Hello, Wolrd!"
# print(a.replace("H", "J"))

# SLICING STRINGS
# b = "Hell 





 


