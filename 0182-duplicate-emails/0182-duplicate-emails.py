import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    counts_df = person.groupby("email").size().reset_index(name="num")
    res = counts_df[counts_df["num"]>1]["email"]
    return pd.DataFrame({"Email":res})