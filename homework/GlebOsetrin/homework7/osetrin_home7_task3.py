def strong_line(line):
    return int(line.split(':')[1]) + 10

my_data = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]
for line in my_data:
    print(strong_line(line))
