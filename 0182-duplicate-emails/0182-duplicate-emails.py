import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    counts = person.groupby("email").size().reset_index(name="num")
    duplicated = counts[counts["num"]>1][["email"]]
    return duplicated