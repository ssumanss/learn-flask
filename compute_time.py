'''
This is an example of a decorator code.
'''

import time

def time_taken(func):
    def wrapper_function():
        t1 = time.time()
        func()
        t2 = time.time()
        return (t2-t1)

    return wrapper_function

@time_taken
def add( ):
    print(2+3)

print(add( ))



