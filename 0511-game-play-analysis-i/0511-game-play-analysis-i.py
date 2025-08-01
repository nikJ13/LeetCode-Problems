import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    dates = activity.groupby("player_id")['event_date'].min().reset_index()
    # res = activity[activity['event_date']==dates][["player_id","event_date"]].rename(columns={"event_date":"first_login"})
    dates = dates.rename(columns={"event_date":"first_login"})
    print(dates)
    return dates