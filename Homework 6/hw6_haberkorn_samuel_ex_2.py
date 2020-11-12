import functools

"""
Assignment: Homework 6, Exercise 2
Name: Samuel Haberkorn
Date: November 11, 2020
Description: The program implements a cache to speed up the process of calculation the fibonacci sequence.
Conclusion: When you are calculating fewer than the first 20 numbers, you do not see much of a difference with the cache.
The performance improvements happen when the numbers are large. Without using that cache, it takes forever to calculate
the 100th number. With a cache, it takes less than 1/10th of a second. Additionally, the number of calls dropped from
millions to just over 100. this makes the time complexity O(n) instead of something exponential.
"""

def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #create a key to base my cache off of
        #make sure it uses all arguments so the decorator can be universal
        key = args.__str__()+kwargs.__str__()
        #check if the return value is cached. If it is return it
        if wrapper.cache.get(key, False):
            return wrapper.cache[key]

        #if the value is not cached, calculate the result
        result = func(*args, **kwargs)
        #then cache the result
        wrapper.cache[key] = result
        return result

    wrapper.cache = {}
    return wrapper


@cache
@countCalls
def fibonacci(num):
    if num<2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

print (fibonacci(100))