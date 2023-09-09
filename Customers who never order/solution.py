import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders["customerId"])].rename(columns={'name':'Customers'})
    if orders.empty:
        return customers["name"].rename('Customers').to_frame()
    else:
        return df["Customers"].to_frame()

find_customers(customers, orders)