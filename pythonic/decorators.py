def decorate(func):
    def inner(*args, **kwargs):
        print("Inside Inner")
        func(args, kwargs)
    # print("Inside decorator")
    return inner


@decorate
def calculate(*args, **kwargs):
    print("Inside print")
    print(*args, **kwargs)

calculate(1,2,3)

# means it is calling like this
# calculate = decorate(calculate)
# calculate(1,2,3)