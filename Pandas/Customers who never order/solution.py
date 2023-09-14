import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders["customerId"])].rename(columns={'name':'Customers'})
    if orders.empty:
        return customers["name"].rename('Customers').to_frame()
    else:
        return df["Customers"].to_frame()