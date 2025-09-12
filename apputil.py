import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
def fibonacci(n):
    '''Return the nth Fibonacci number.'''
    if n <= 0:
        print("Input should be a positive integer.")
        return None
    elif n == 1:
        print (0)
    elif n >= 2: 
        return 