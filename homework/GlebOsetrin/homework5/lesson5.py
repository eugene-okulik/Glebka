person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name = 'John'
last_name = 'Doe'
city = 'New York'
phone = '+1372829383739'
country = 'US'
# я не понял первое задание :( перевел дословно и сделал дословно
# и есть ли разница в питоне между " и '
result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'
colon_position1 = result1.index(':')
number1_str = result1[colon_position1+2:]
number1 = int(number1_str)
print(number1 + 10)

colon_position2 = result2.index(':')
number2_str = result2[colon_position2+2:]
number2 = int(number2_str)
print(number2 + 10)

colon_position3 = result3.index(':')
number3_str = result3[colon_position3+2:]
number3 = int(number3_str)
print(number3 + 10)

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
my_text = 'Students {} study these subjects: {}'
my_text = my_text.format(', '.join(students), ', '.join(subjects))
# я не знаю откуда появилось args, оно почему-то ставится автоматически в пайчарме и не удаляется
print(my_text)
