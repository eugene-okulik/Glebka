def finish_me(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('finished')
        return result
    return wrapper

@finish_me
def example():
    print('I love python')

@finish_me
def example2():
    print('very much')

@finish_me
def example3():
    print('and python is very good programm')

example()
example2()
example3()
