import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_1 = world[world["population"] >= 25_000_000]
    df_2 = world[world["area"] >= 3_000_000]
    frames = [df_1, df_2]
    result = pd.concat(frames)
    return result.drop(columns=["continent","gdp"])