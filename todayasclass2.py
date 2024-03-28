
# Python Regular Expression
# RegEx or Regular Expression is a sequence of character that forms partern of search.

# import re
# Check to see if the statement starts with 'the' and ends with 'it'
# text = """the value of a thing will determing the capacity you put to it"""

# Python String class
# if text.startswith("the") and text.endswith("it"):
#     print("we have a match")
# else:
#     print("No match detected")

# Python Regular expression
# val = re.search("^the.*it$", text)
# print(val)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")

# re function
# findall(): returns list containing all matches
# search(): returns object of a match if there is a match anywhere in the string
# split(): returns a list where the string has been split at each match
# sub(): replace one or many matches  with a string

# re matacharacters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special charactter eg "\d" 
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

# comment = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021"""

# match = re.search("of*", comment)
# if match:
# 	print(match)
# else:  
# 	print("no match detected")

# match = re.findall("of", comment)
# if match:
# 	print(match)
# else:
# 	print("no match detected")

# match = comment.split()
# if match:
#    print(match)

#  


# re special Sequences
# \A : returns a match if the specified characters are at the begining of the string eg "\AThe"
# \b : returns a match if the specified characters are at the begining or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the begining or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contains digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contains a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w" 
# \W : returns a match where the string does not contains any word characters 
# \Z : returns a match if the specified characters are at the end of the string

# re sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string

comment = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021"""

# phone_num = ['080434343433', '09023343656', '07023343656', '08023343656', '09023343656']

# x = re.findall('you', comment)
# print(x)
x = re.findall(r'you', comment)
# print(x)
# x = re.search(r'you', comment)
# print(x)
# print(x.span())
# print(x.group()) 
# print(x.string)

#comment = """the value of a thing will determing the capacity you put to it. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021"""
# z = re.split(r'\s', comment)
# print(z)
# z = re.split(r'\s', comment, 5)
# # print(z)
# tx = re.sub(r'\d', '1980', comment)
# print(tx)
# tx = re.sub(r'[0-9][0-9][0-9][0-9]', '1980', comment)
# print(tx)
# tx = re.sub(r'capacity', 'ability', comment)
# print(tx)
# tx = re.sub(r'[123]', '[]', comment, 4)
# print(tx)
# phone_num = [re.sub(r'[0]', '123', phone, 1) for phone in phone_num]
# print(phone_num)