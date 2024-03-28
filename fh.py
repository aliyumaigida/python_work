
#  File Handling

# myFile = open("filename", mode='r', 'a', 'w','x', encoding='t','b')
# 'r' read only and it is the default for open function. Raise error if file does not exist
# 'a' Append new content to an existing file. Create new file with the specified name if file does not exist.
# 'w' Open file for writing. Create new file with the specified name if file does not exist
# 'x' To create new file. Raise error if file already exist

# myfile.close()
# with open("filename", mode="rt") as myFile:
# myFile = open("c:\\Users\\Aliyu 2.0\\Desktop\\practice\\New Text Document.txt", 'rt')
# myFile.read()
# print(myFile)
# print(myFile.read())
# print(myFile.read(20)) # read the first 20 characters in the file
# print(myFile.readline())
# for i in range(20):
#     print(myFile.readline())

# for text in myFile:
#     print(text)

# myFile.close()
# print(myFile.closed)
# myfile =open("file1.txt", "r")
# print("file created successfully.")
# myfile.write("Today is a boring day for me\n i am not Happy today")
# print("the file has been added successfully")
# print(myfile.read())

# using with open function
# with open("infile.txt", mode="rt") as myFile:
#     print(myFile.read())
# myFile = open("infile.txt", 'w')
# print(myFile.read())
# myfile =open("onlyfile.txt", 'r')
# print(myfile.read())
# myfile.write("\nBe nice to me.")
# print('text appended successfully')
# print('onlyfile create successfully..')
# myFile.write("\n Hello eveyone, this is my first file working currently.")
# print("text appended successfuly")


# myFile = open("file2.txt", 'a')
# myFile.write("\n this is to append a new content to the file")
# print("text appended successfuly")

# myFile = open("file2.txt", 'rt')
# print(myFile.read())
# myFile.close()

# content = ""
# myFile = open("file2.txt", 'a')
# content += myFile.read()
# myFile.close()
# content = content.replace("this is to append a new content to the file", "")
# myFile = open("file2.txt", "r")
# myFile.write('this is to append a new content to the file')
# print('file has been added successfully.')
# myFile.write(content)
# print(content)
# print(myFile.read())



# myFile = open("file2.txt", 'rt')
# # print(myFile.read())
# print(myFile.readline())
# for i in myFile:
#     print(i)
# myFile.close()

# myFile = open("Aliyu.txt", 'rt')
# myFile.write("This is my firsy file\nHello world")
# print(myFile.readline)
# print("File created successfully")


import os

# if os.path.exists("newfile.txt"):
# 	with open("newfile.txt", mode="rt") as myFile:
# 		for i in myFile:
# 		  print(i)
# else:
#     print("file does not exits")
#     with open("newfile.txt", mode="xt") as myFile:
#         myFile.write("this is the check if a file exists and read from it else create the file and write to it.")
#         print("file created successfully")

# if os.path.exists("newfile.txt"):
#     os.remove("newfile.txt")
#     print("file deleted successfully")
# else:
#     print("file not available.")

# os.mkdir("C:\\Pandas")
# print("folder created successfully")

# os.rmdir("C:\\Users\\Hp\\Documents\\pythonclass folder")
# print("folder deleted successfully")

# print(os.listdir("pythonclass folder"))

# code to remove folder containing contents in it
# os.rmdir("pythonclass folder")
# print("folder deleted successfully")

# import time
# for root, dirs, files in os.walk("pythonclass folder"):
#     print("Wait while folder are being delete")
#     time.sleep(2)
#     for dir in dirs:
#         os.rmdir(root+"\\"+dir)
#     print("Wait while files are being delete")
#     time.sleep(2)    
#     for file in files:
#     	os.remove(root+"\\"+file)
# # 
# print("Wait while main folder are being delete")
# time.sleep(2)
# os.rmdir(root)

# Code to delete from folder that contains contents in its inner folders
# import os
# import time
# for root, dirs, files in os.walk("pythonclass folder"):

#     for folder in dirs:
#         for rot, fold, file in os.walk(root+'\\'+folder):
#             print("Wait while inner folders are being delete")
#             for file in file:
#                 os.remove(root+"\\"+folder+"\\"+file)
        
#         print("Wait while folders are being delete")
#         time.sleep(2)
#         os.rmdir(root+"\\"+folder)
    
#     print("Wait while files are being delete")
#     time.sleep(2)  
#     for file in files:
#     	os.remove(root+"\\"+file)

# print("Wait while main folder are being delete")
# time.sleep(2)
# os.rmdir("pythonclass folder")


# code to get username of any system(pc)
# import os.path
# homedir = os.path.expanduser("~")
# print(homedir)
# print(homedir+"\Downloads")

# code to get system environment
# import os
# homedir = os.environ["PATH"]
# print(homedir)

# code to get the path of a file on your device
# import os
# print(os.path.abspath("C++ course outline.txt"))
# print(os.path.dirname(os.path.abspath("infile.txt")))

# import os
# image = []
# target_name = []
# for root, dirs, files in os.walk("C:\\PythonClass\\Data Science\\Datasets\\lfw_funneled"):
#     for folder in dirs:
#         for rot, fold, file in os.walk(root+'\\'+folder):
#             for img in file:
#                 target_name.append(os.path.basename(img))
#                 image.append(root+'\\'+folder+'\\'+img)
# # print(image)
# print(len(target_name))
# print(len(image))
# print(target_name)


# simple code to rename file name in a folder of another folder
# import os
# image_path = "C:\\pythonclass\\Students Assignments\\assigmentProject\\Agro360 project\\Main project\\Dataset\\train"
# i = 1
# for root, dirs, files in os.walk(image_path):
#     for folder in dirs:
#         for rot, fold, file in os.walk(root+'\\'+folder):
#             i = 1
#             for img in file:
#                 os.rename(root+'\\'+folder+"\\"+os.path.basename(img), root+'\\'+folder+"\\"+os.path.basename(root+'\\'+folder)+"_"+str(i)+".jpg")
#                 i+=1