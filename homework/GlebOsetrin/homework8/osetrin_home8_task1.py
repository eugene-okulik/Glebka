import random

salary = int(input("Enter your salary: "))
bonus = random.choice([True, False])
if bonus:
    bonus_numb = random.randint(1, 50000)
    salary += bonus_numb
print(f'Bonus number: {bonus}')
print(f'Salary: {salary}')