import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    
    # Create copy of employee
    df = employee

    # Merges rows
    df = df.merge(df, left_on='managerId', right_on='id', suffixes=('', '_manager'))

    # Managers don't have managers so this column is redundant
    df = df.drop(columns=["managerId_manager"])

    # Create a new column that stores a query
    df["paid_more"] = df["salary"] > df["salary_manager"]

    # Take all the rows that are True
    filtered_df = df[df['paid_more'] == True]

    # Take the value stored in the 'name' column
    names = filtered_df['name']

    # Convert names from a Series to a frame because it is required by leetcode to return Dataframe
    names = names.to_frame()

    # Rename "names" column to "Employee", because it is also required by leetcode
    names = names.rename(columns={'name': 'Employee'})

    # return dataframe
    return names
    
find_employees(pd.read_csv("pay.csv"))
