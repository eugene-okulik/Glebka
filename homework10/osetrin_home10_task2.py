def repeat_me(func):
    def wrapper(text, count=3):
        for x in range(count):
            func(text)
    return wrapper

@repeat_me
def example(text):
    print(text)

@repeat_me
def example2(number):
    print(number)

example('print me', count=2)
example2(5, count=6)
