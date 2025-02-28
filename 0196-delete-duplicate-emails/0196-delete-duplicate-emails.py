import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby("email")["id"].transform("min")
    removed = person[person["id"]!=min_id]
    person.drop(removed.index, inplace=True)
    return