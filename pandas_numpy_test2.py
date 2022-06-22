import pandas as pd
import numpy as np
import time

# a simple function to print after the operations
def thanks():
    print('Thanks for using this operation')
    print()
    time.sleep(2)

# check for existence of a column
def ask_column(l):
    print()
    column_name = input("Enter the columns name ").strip()
    if not check_column(l, column_name):
        print('You entered a wrong column that was not there in the dataset please verify and enter the right code next time')
        time.sleep(1)
        return False
    return column_name

#check for the existence of the columnname
def check_column(l, column_name):
    if column_name in l:
        return True
    else:
        return False

#provide the destination of the file here
df = pd.read_csv('test2.csv')
df_backup = pd.DataFrame(df)
print(df)
l = list(df.columns)#list of all the columns present inside the excel sheet

while True:
    s = '''The following are the features available that can be performed in the dataset
    1. The mean of a specific column available in the given input file.
    2. The median of a specific column available in the given input file.
    3. Filter all the records exactly matching a value on a specific column in the given input file.
    4. Filter All the records distributed in a range of 5% around the given input for the column.
    5. Calculate the change in values for specific column in the given input file along with it find average change, maximum change, minimum change.
    ** ENTER ANY OTHER KEY TO EXIT
    '''
    print(s)
    n = int(input("Enter your choice: ").strip())
    df = pd.DataFrame(df_backup) #incase the columns have been modified by any operation

    if n == 1:
        print(f'You have chosen option {n}')
        print()
        column_name = ask_column(l)
        if not column_name:
            continue
        #numpy mean to calculate the mean
        col_mean = np.mean(df[column_name])
        print(f'The mean of the column {column_name} is {col_mean}')
        thanks()

    elif n == 2:
        print(f'You have chosen option {n}')
        print()
        column_name = ask_column(l)
        if not column_name:
            continue
        #numpy median to calculate the median
        col_median = np.median(df[column_name])
        print(f'The mean of the column {column_name} is {col_median}')
        thanks()

    elif n == 3:
        print(f'You have chosen option {n}')
        print()
        column_name = ask_column(l)
        if not column_name:
            continue
        val = input('Enter the value: ')
        if val in set(df[column_name].map(str)):
            df2 = df[df[column_name].map(str).str.contains(val)]
            print(df2)
        else:
            print(f'The value {val} was not present in the column {column_name}')
        print()
        thanks()

    elif n == 4:
        print(f'You have chosen option {n}')
        print()
        df2 = df
        column_name = ask_column(l)
        if not column_name:
            continue
        val = float(input('Enter the value: '))

        #creating the main logic to caculate the 5% difference 
        df2['5%'] = ((df2[column_name]-val)/val)*100
        df3 = df2.loc[(df2['5%'] >= 0) & (df2['5%'] <= 5)]

        if not df3.empty:
            print('The values around 5% of difference are :')
            print(df3)
        else:
            print('No such values exit around 5% interval')
        print()
        thanks()

    elif n == 5:
        print(f'You have chosen option {n}')
        print()
        column_name = ask_column(l)
        if not column_name:
            continue
        df2 = df
        #creating a diff column to mark the difference of values from the previous row
        df['diff'] = np.nan
        #findng difference
        for x in list(df.index)[1:]:
            df.loc[x, 'diff'] = df.loc[x, column_name]-df.loc[x-1, column_name]
        
        print("Successfully calculated the difference")
        print(
            f"The average of the values after finding difference is: {df['diff'].sum()/len(l)}")
        print(
            f"The maximum of the values after finding difference is: {df['diff'].max()}")
        print(
            f"The minimum of the values after finding difference is: {df['diff'].min()}")
        df = df2
        print()
        thanks()

    else:
        print(f'You have chosen option {n}')
        print()
        print('Thankyou for using this code')
        break
