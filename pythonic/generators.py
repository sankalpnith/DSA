# Python generators are a simple way of creating iterators.  generator fxn return iterators any fxn having yield is a generator
#1. Easy to Implement
#Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.
# Following is an example to implement a sequence of power of 2 using an iterator class.

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result
#The above program was lengthy and confusing. Now, let's do the same using a generator function.

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# 2. Memory Efficient
# A normal function to return a sequence will create the entire sequence in memory before returning the result. This is an overkill,
# if the number of items in the sequence is very large.
#
# Generator implementation of such sequences is memory friendly and is preferred since it only produces one item at a time.

#Represent Infinite Stream
#Generators are excellent mediums to represent an infinite stream of data. Infinite streams cannot be stored in memory,
# and since generators produce only one item at a time, they can represent an infinite stream of data.
#The following generator function can generate all the even numbers (at least in theory).

def all_even():
    n = 0
    while True:
        yield n
        n += 2
