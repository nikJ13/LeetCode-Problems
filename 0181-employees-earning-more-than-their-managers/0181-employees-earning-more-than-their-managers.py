import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(employee, left_on="managerId", right_on="id", suffixes=("","_manager"))
    names = merged_df.loc[merged_df["salary"]>merged_df["salary_manager"],["name"]]["name"]
    return pd.DataFrame({"Employee":names})