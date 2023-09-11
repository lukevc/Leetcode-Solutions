import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicateRows = person.loc[person.duplicated(subset=['email']), ['email']]
    return duplicateRows.drop_duplicates()
    
print(duplicate_emails(pd.read_csv("data.csv")))