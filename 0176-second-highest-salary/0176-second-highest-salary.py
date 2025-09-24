import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries_ordered = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(unique_salaries_ordered)<2:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [unique_salaries_ordered.iloc[1]]})