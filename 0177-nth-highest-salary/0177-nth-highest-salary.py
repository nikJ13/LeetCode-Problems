import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    uniques = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(uniques)<N or N<=0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})
    else:
        return pd.DataFrame({f"getNthHighestSalary({N})":[uniques.iloc[N-1]]})