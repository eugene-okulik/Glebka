
list1 = [1, 5, 15, 28, 'brother', 'sister', 'dog', 25.5, 'cat', 'Yes', False]
list1.append('tatos')
list1.pop(1)

tuple1 = (10, 20, 30, 'frog', 'shark')
print(tuple1[-1])

set1 = {4, 8, 12, 16.5, 'very_fun', True}
set1.add('song')
set1.remove(12)

dict1 = {
    'My name': 'Gleb',
    'My surname': 'Osetrin',
    'My age': '30',
    'My job': 'QA Engineer',
    'My hobby': 'swim'
}

dict1[('i am a tuple',)] = 'New word'
dict1.pop('My hobby')

mydict = {'list': list1, 'tuple': tuple1, 'set': set1, 'dict': dict1}
print(mydict)
