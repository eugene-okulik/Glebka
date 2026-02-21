def decorator(func):
    def wrapper(a, b):
        if a < 0 or b < 0:
            return func(a, b, '*')
        elif a == b:
            return func(a, b, '+')
        elif a > b:
            return func(a, b, '-')
        elif a < b:
            return func(a, b, '/')
    return wrapper

@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second

print(calc(3, 4))
print(calc(5, 5))
print(calc(5, 4))
print(calc(-3, 4))