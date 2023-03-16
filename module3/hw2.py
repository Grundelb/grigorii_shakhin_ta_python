"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable

def cache(func: Callable) -> Callable:
    '''
    The wrapper function first checks whether the arguments are already in the cache. If they are, it returns the cached result. 
    Otherwise, it calls the original function func with the given arguments and stores the result in the cache before returning it.
    '''
    cache_dict = {}

    def wrapper(*args):
        if args in cache_dict:
            return cache_dict[args]
        else:
            result = func(*args)
            cache_dict[args] = result
            return result

    return wrapper
