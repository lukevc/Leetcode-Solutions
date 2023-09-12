import pandas as pd

data = [[1, 1], [2, 2], [3, 3], [4, 3]]
orders = pd.DataFrame(data, columns=['order_number', 'customer_number']).astype({'order_number':'Int64', 'customer_number':'Int64'})

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby('customer_number').size().reset_index()
    orders = orders.sort_values(by=0, ascending=False)
    if orders.empty:
        return orders["customer_number"].to_frame()
    else:
        data = orders["customer_number"].iloc[0]
        return pd.DataFrame(
            {"customer_number" : [data] }
        )