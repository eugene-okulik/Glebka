operation1 = 'результат операции: 42'
operation2 = 'результат операции: 514'
operation3 = 'результат работы программы: 9'

colon_index1 = operation1.index(':')
number_str1 = operation1[colon_index1 + 2:]
number = int(number_str1)
result = number + 21
print(result)

colon_index2 = operation2.index(':')
number_str2 = operation2[colon_index2 + 2:]
number = int(number_str2)
result = number + 21
print(result)

colon_index3 = operation3.index(':')
number_str3 = operation3[colon_index3 + 2:]
number = int(number_str3)
result = number + 21
print(result)
