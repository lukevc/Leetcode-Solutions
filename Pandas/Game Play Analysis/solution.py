import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity_agg = (
    activity.groupby("player_id", as_index=False).agg(event_date = pd.NamedAgg(column="event_date", aggfunc="min"))
    .rename(columns={"player_id":"player_id", "event_date":"first_login"})
    )
    return activity_agg