import pandas as pd

data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype({'name':'object', 'continent':'object', 'area':'Int64', 'population':'Int64', 'gdp':'Int64'})

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_1 = world[world["population"] >= 25_000_000]
    df_2 = world[world["area"] >= 3_000_000]
    frames = [df_1, df_2]
    result = pd.concat(frames)
    return result.drop(columns=["continent","gdp"])