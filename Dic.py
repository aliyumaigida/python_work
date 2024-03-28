
# DICTIONARY is a collection wich is ordered, changeable but does not allow duplicate and unindex values

# vehicle = {'Name': 'Toyota', 
#            'Model': 'Highlander', 
#            'color': ['green', 'Black' ],
#            'year': 2022,
#            'new': True}
# print(type(vehicle))
# print(vehicle)
# vehicle['year'] = 2023
# print(vehicle)
# print(vehicle.keys())
# print(vehicle.values())
# print(vehicle.items())
# x=vehicle.pop('color')

# print(x.__doc__)


# for each in vehicle.values():
    # print(each)
# for  x, y in vehicle.items():
#  print(f'{x}: {y}')
# duplicate = vehicle.copy()
# duplicate['year'] = 2023
# print(duplicate)
# print(vehicle)
# print(vehicle.get('year'))
# print(vehicle.fromkeys('year', 2023))?
# vehicle.pop('year')
# vehicle.popitem(('year', 2023))
# vehicle.update({'transmission': 'automatic'})
# print(vehicle)




Q_and_A = {
    'C':'Who is the president of Nigeria\n\na:buhari\nb:JAGABAN\nc:bat',
    'A':'What is the capital of Nigeria\na:ABUJA\nb:Uyo\nc:Oyo',
    'B':'How many state are in nigeria\na:24\nB:36\nc:34'
}
score = 0
for answer,question in Q_and_A.items():
    print(question, '\n')
    user = input('answer:')
    if user.upper()== answer:
        print('correct')
        score+=5
        print(score)
    else:
        print('incorrect')

        print('Your score is', score)

# x='water'
# print(x.upper())
