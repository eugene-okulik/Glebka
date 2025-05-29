
List = [1, 5, 15, 28, 'brother', 'sister', 'dog', 25.5, 'cat', 'Yes', False]
List.append('tatos')
List.pop(1)

Tuple = (10, 20, 30, 'frog', 'shark')
print(Tuple[-1])

Set = {4, 8, 12, 16.5, 'very_fun', True}
Set.add('song')
Set.remove(12)

Dict ={'My name': 'Gleb',
        'My surname': 'Osetrin',
        'My age': '30',
        'My job': 'QA Engineer',
        'My hobby': 'swim'
     }

Dict[('i am a tuple',)] = 'New word'
Dict.pop('My hobby')

mydict = {'list': List, 'tuple': Tuple, 'set': Set, 'dict': Dict}
print(mydict)
