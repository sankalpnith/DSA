# Decorators allow us to extend the behaviour of wrapped function without permanently modifying it
def decorate(func):
    def inner(*args, **kwargs):
        print("Inside Inner")
        print(args, kwargs)
        func(args, kwargs)
    # print("Inside decorator")
    return inner


def decorate1(func, *args, **kwargs):
    print("decorate1")
    print(*args, **kwargs)
    return func


@decorate
def calculate(*args, **kwargs):
    print("Inside print")
    print(*args, **kwargs)

calculate(1,2,3)

# means it is calling like this
# calculate = decorate(calculate)
# calculate(1,2,3)

#we can also define decorators without specifying inner function. Inner function is used to pass the decorated fxn arguments like
def outer(func):
    def inner(*args, **kwargs):
        print('Hi my name is ')
        return func(*args, **kwargs)
    return inner

@outer
def decorated(name):
    print(name)

Here when I call
decorated("sankalp") -> outer(decorated)("sankalp")