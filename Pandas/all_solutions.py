import pandas as pd

""" Employees that are Earning more than their managers """

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee
    df = df.merge(df, left_on='managerId', right_on='id', suffixes=('', '_manager'))
    df = df.drop(columns=["managerId_manager"])
    df["paid_more"] = df["salary"] > df["salary_manager"]
    filtered_df = df[df['paid_more'] == True]
    names = filtered_df['name']
    names = names.to_frame()
    names = names.rename(columns={'name': 'Employee'})
    return names


""" Returns a list of duplicate emails """

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicateRows = person.loc[person.duplicated(subset=['email']), ['email']]
    return duplicateRows.drop_duplicates()


""" Drop duplicate emails from a database inplace """

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',ascending=True,inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)


""" Return a list of customers who never order """

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders["customerId"])].rename(columns={'name':'Customers'})
    if orders.empty:
        return customers["name"].rename('Customers').to_frame()
    else:
        return df["Customers"].to_frame()
    

""" Returns the customer with the highest number of orders """    

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
    

""" Finds countries from a list of countries that meet "big country" requirements """

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_1 = world[world["population"] >= 25_000_000]
    df_2 = world[world["area"] >= 3_000_000]
    frames = [df_1, df_2]
    result = pd.concat(frames)
    return result.drop(columns=["continent","gdp"])


""" Finds the first login in date for each player """

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_agg = (
    activity.groupby("player_id", as_index=False).agg(event_date = pd.NamedAgg(column="event_date", aggfunc="min"))
    .rename(columns={"player_id":"player_id", "event_date":"first_login"})
    )
    return activity_agg