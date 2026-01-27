ttuple = (1, 5, 51, 'money', 'six', False)
listt = [1, 5, 51, 'money', 'six', False, 2, 99, True]
sset = {2, 5, 8, 11, 'six', 'five', 'big', 25, False}
dictt = {
    'name': 'Gleb',
    'sername': 'Osetrin',
    'age': '30',
    'hobby': 'work',
    'city': 'Perm'
}
my_dict = {'list': listt, 'tuple': ttuple, 'set': sset, 'dict': dictt}

print(ttuple[-1])
listt.append('text')
listt.pop(1)
dictt[('i am a tuple',)] = 'key1'
dictt.pop('age')
sset = {2, 5, 8, 11, 'six', 'five', 'big', 25, False}
sset.add('winter')
sset.remove(2)

print(my_dict)
