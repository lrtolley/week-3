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

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url)

#used df_bellevue['gender'].value_counts() to find the issue
#with the gender column as outlined in the problem set
df_bellevue['gender'].replace('?', np.nan, inplace=True) #replacing non-gender values with NaN
df_bellevue['gender'].replace('g', np.nan, inplace=True)
df_bellevue['gender'].replace('h', np.nan, inplace=True)
df_bellevue['gender'].value_counts() #checking to make sure the replacements worked

def task_i1():
    '''returns a list of column names 
    sorted by ascending missing values'''
    null_counts = df_bellevue.isnull().sum() #creates a series with the count of missing values for each column
    columns_na = null_counts.sort_values(ascending = True) #sorts the series by ascending missing values
    print(columns_na)

def task_i2():
    '''creates a dataframe with the year and number of entries'''


def task_i3():
    '''
    return a series that indexes the gender 
    and the average age for each gender
    '''
    return df_bellevue.groupby('gender')['age'].mean()

def task_i4():
    '''returns the top 5 most common occupations in descending order'''
    return df_bellevue['profession'].value_counts().head(5)