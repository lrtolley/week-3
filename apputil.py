import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
def fibonacci(number):
    '''Return the nth Fibonacci number.'''
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def to_binary(number):
    '''Convert a positive integer to binary using recursion.'''
    if n < 0:
        return None
    elif n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)


url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'
df_bellevue = pd.read_csv(url) #reads in the csv file from the url

#used df_bellevue['gender'].value_counts() to find the issue
#with the gender column as outlined in the problem set
df_bellevue['gender'].replace('?', np.nan, inplace=True) #replacing non-gender values with NaN
df_bellevue['gender'].replace('g', np.nan, inplace=True)
df_bellevue['gender'].replace('h', np.nan, inplace=True)
df_bellevue['gender'].value_counts() #checking to make sure the replacements worked

def task_1():
    '''Return list of column names sorted by ascending missing values.'''
    null_counts = df_bellevue.isnull().sum()
    sorted_columns = null_counts.sort_values().index.tolist()
    return sorted_columns


def task_2():
    '''Return DataFrame with year and total_admissions.'''
    df_bellevue[['year', 'month', 'day']] = df_bellevue['date_in'].str.split('-', expand=True)
    year_counts = df_bellevue['year'].value_counts().sort_index()
    result = year_counts.rename('total_admissions').reset_index()
    result.columns = ['year', 'total_admissions']
    return result


def task_3():
    '''
    returns a series that indexes the gender 
    and the average age for each gender
    '''
    return df_bellevue.groupby('gender')['age'].mean()
#sorts by (corrected) genders and returns average age

def task_4():
    '''Return list of top 5 most common professions.'''
    df_bellevue['profession'] = df_bellevue['profession'].astype(str).str.lower()
    df_bellevue['profession'] = df_bellevue['profession'].str.replace(" ", "", regex=False)
    df_bellevue['profession'] = df_bellevue['profession'].str.replace("-", "", regex=False)
    top_5 = df_bellevue['profession'].value_counts().head(5).index.tolist()
    return top_5
