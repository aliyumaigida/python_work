todo_list = []
print('My To_Do list Application')

user = input("""
1. Create a TO_Do list
2. Exit           
\nChoice: """)
if user == '1':
  while True:
    user1= input('1. Add to list\n2. Edit an item\n3. REmove an item\n4. Delete list\n5. view To Do list\n6. Exit\n\nYour choice: ')

    if user1 == "1":
      add_list = input(" Add To Do:")
      todo_list.append(add_list)
      print(len(todo_list))
    elif user1 == "2":
      print(todo_list)
      user2 = input('''item to edit''')
      todo_list.insert(2,user2)
      print(todo_list)
    elif  user1 == '3':
      print(todo_list)
      u=input('Select and write the item to remove:')
      todo_list.remove(u)
      print(todo_list)

    elif user1 == '4':
      print(todo_list)
      todo_list.clear()
      print('You have successfully empty todo_list\n')
      print(todo_list) 

    elif user1 == '5':
      print(todo_list)   

    elif user1 == '6':
      exit()

else:
   print('invalid option')



        