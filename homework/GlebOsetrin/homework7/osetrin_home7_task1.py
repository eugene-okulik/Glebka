my_number = 5
while True:
    user_input = int(input('Пожалуйста, введите ваше число: '))
    if user_input != my_number:
        print('попробуйте снова')
    else:
        break
print('Поздравляю! Вы угадали!')
