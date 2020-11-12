from time import sleep
import functools

"""
Assignment: Homework 6, Exercise 1
Name: Samuel Haberkorn
Date: November 11, 2020
Description: This program implements a decorator that delays the execution of a function by a time supplied in the decorator
"""



def slowDown(_func=None, *, time=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sleep(time)
            return func(*args, **kwargs)
        return wrapper
    #to handle no args given
    return decorator if _func is None else decorator(_func)



@slowDown(time = 2)
# from lecture
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)


if __name__ == '__main__':
    countdown(5)