import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
def fibonacci(n):
    '''Return the nth Fibonacci number.'''
    if n <= 0: #this is to handle invalid input 
        print("Input should be a positive integer.")
        return None
    elif n == 1: #defines the first Fibonacci number
        return 0
    elif n == 2: #defines the second Fibonacci number
        return 1
    else: #recursive case to calculate the nth Fibonacci number above n=2
        return fibonacci(n-1) + fibonacci(n-2) 

def to_binary(number):
    '''Converts a positive integer base 10 number to a binary number'''
    if number == 0: #defines 0 in binary
        return "0"
    if number < 0: #prevents negative input 
      print("Input should be a positive integer.")
        return None
    binary_digits = []
    dividend = number
    while dividend > 0:
        quotient, remainder = divmod(dividend, 2) #divides the number by 2 and gets the quotient and remainder
        binary_digits.insert(0, str(remainder)) #inserts the remainder in the frontmost position of the list
        dividend = quotient #updates the dividend to be the quotient for the next iteration
    return "".join(binary_digits) #joins the list of binary digits into a string and returns it

def task_i():
    '''returns a list of column names 
    sorted by ascending missing values'''