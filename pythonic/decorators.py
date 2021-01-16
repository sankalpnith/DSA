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