tupleone = (1, 5, 51, 'money', 'six', False)
# print(tupleone[-1])

listone = [1, 5, 51, 'money', 'six', False, 2, 99, True]
listone.append('text')
listone.pop(1)
# print(listone)

dictone = {'name' : 'Gleb',
           'sername' : 'Osetrin',
           'age' : '30',
           'hobby' : 'work',
           'city' : 'Perm'
}
# print(dictone)
dictone['i am a tuple'] = 'key1'
# print(dictone)
dictone.pop('age')
# (dictone)

setone = {2, 5, 8, 11, 'six', 'five','big', 25, False}
setone.add('winter')
# print(setone)
setone.remove(2)
# print(setone)

my_dict = {'list' : 'value1', 'tuple' : 'value2', 'set': 'value3', 'dict': 'value3'}
# print(my_dict['set'])
# my_dict['five'] = True
# my_dict['six'] = {1, 7, 33}
