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
    binary_digits = [] #starts an empty list to hold the binary digits
    dividend = number
    while dividend > 0:
        quotient, remainder = divmod(dividend, 2) #divides the number by 2 and gets the 
        #quotient and remainder
        binary_digits.insert(0, str(remainder)) #inserts the remainder in the frontmost 
        #position of the list
        dividend = quotient #updates the dividend to be the quotient for the next iteration
    return "".join(binary_digits) #joins the list of binary digits into a string and returns it

url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url) #reads in the csv file from the url

#used df_bellevue['gender'].value_counts() to find the issue
#with the gender column as outlined in the problem set
df_bellevue['gender'].replace('?', np.nan, inplace=True) #replacing non-gender values with NaN
df_bellevue['gender'].replace('g', np.nan, inplace=True)
df_bellevue['gender'].replace('h', np.nan, inplace=True)
df_bellevue['gender'].value_counts() #checking to make sure the replacements worked

def task_1():
    '''returns a list of column names 
    sorted by ascending missing values'''
    null_counts = df_bellevue.isnull().sum() #creates a series with the count of missing values for each column
    columns_na = null_counts.sort_values(ascending = True) #sorts the series by ascending missing values
    return columns_na

def task_2():
    '''creates a dataframe with the year and number of entries'''
    df_bellevue[['year', 'month', 'day']] = df_bellevue['date_in'].str.split('-', expand=True)
    dates_to_count = df_bellevue['year'].value_counts() #creates a series with the count of 
    #entries for each year
    dframe_dates = pd.DataFrame(dates_to_count) #converts the series to a dataframe
    renamed_frame = dates_to_count.rename('total_admissions').to_frame()
    #renames the count 
    #column to total_admissions
    return renamed_frame

def task_3():
    '''
    returns a series that indexes the gender 
    and the average age for each gender
    '''
    return df_bellevue.groupby('gender')['age'].mean()
#sorts by (corrected) genders and returns average age

def task_4():
    '''returns the top 5 most common occupations in descending order'''
    df_bellevue['profession'] = df_bellevue['profession'].astype(str).apply(lambda x: x.lower())
    df_bellevue['profession'] = df_bellevue['profession'].str.replace(" ", "", regex=False)
    df_bellevue['profession'] = df_bellevue['profession'].str.replace("-", "", regex=False)

    # Get top 5 most common professions
    sortedvalues = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return sortedvalues