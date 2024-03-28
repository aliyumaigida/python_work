# A set is a collection which is unordered, unindex, unchangeable and does not accept duplicate values


name={'Habib','Aliyu', 'Daniel', 'Josh', 'dare', 'Andrew'}
# print(type(name))
# print(name)
# name.add("Mayowa")
# name.discard('dare')
# name.difference()
# print(name)

newname = ('Muazeem', 'Noah', 'Josh', 'Opeyemi')
# name.update(newname)
# print(name)

# name1 = name.intersection(newname)
# print(name1)
# name.remove('Daniel')
# print(name)
# name.discard('dare')
# print(name)

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set2 = {2, 3, 4}
# x=set1.difference(set2)
# print(x)
set3 = {5, 7, 8, 9}
set4 = set1 - set2
# print(set4)
set4 = set1.union(set2)
# print(set4)
intersect = set1.intersection(set2)
intersect = set1.intersection(set2).intersection(set3)
print(intersect)

# set1.intersection_update(set2)
# print(set1)
# set4=set2.symmetric_difference(set1)
# set4=set2.symmetric_difference_update(set1)
# print(set4)

# set4 =set1.difference(set2)
# print(set4)
# print(set1.isdisjoint(set2))
# print(set1.issuperset(set2))
# print(set1.issubset(set2))

# # SET LIST

# num_of_set = int(input('How many set do you have:'))
# list_set = []
# y = 0
# for num in range(1, num_of_set+1):
#     list_set.append(set())
#     num_item = int(input(f'How many items do you have in set{num}: '))
# items =[]
# x =1
# for x in range(num_item):
#     item = int(input(f'item{x}:'))
#     items.append(item)
#     x+=1

#     list_set[y] = set((items))
#     y+=1
# z =1
# for each_set in list_set:
#         print(f'''
# set{z}: {each_set}
# ''')
#         z+=1

# print('''
#           1. Union
#           2. Intersection
#           ''')
# user = input('option:')
# if user == '1':
#     print('setA union setB')
#     setA = (type('What is your setA:'))
#     setB = (type('What is your setB:'))
#     setA = set(list_set[setA - 1])
#     setB = set(list_set[setB -1])
#     print(f'{setA} union{setB} = {setA.union(setB)}')

# elif user == '2':
#     print('setA intersection setB')
#     setA = int(input('What is your setA:'))
#     setB = int(input('What is your setB:'))
#     setA = int(list_set[setA - 1])
#     setB = int(list_set[setB - 1])
#     print(f'{setA} intersection {setB} = {setA.intersection(setB)}')

# else:
#     print('Invalid option')

