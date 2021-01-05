# lambda returns a function object not the return value ex lambda x,y: x+y it returns a fxn which calculates x+y
# map(function, iterable(s)) it returns map object which is also an iterable
#The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.

a = map(int, ['1','2'])
print(list(a)) # [1,2]


#filter () forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True
# returns filter object which is an iterable
a = filter(lambda x : x[0]=='a', ['abc','def'])
print(list(a)) # ['abc']

#reduce() works by calling the function we passed for the first two items in the sequence.
# The result returned by the function is used in another call to function alongside with the next (third in this case), element.

from functools import reduce
a = reduce(lambda x,y: x+y, [2,1,2,3] )
print(a) # 8