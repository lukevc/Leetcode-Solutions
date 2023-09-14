import pandas as pd

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