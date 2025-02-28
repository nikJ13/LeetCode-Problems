import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, how="inner", left_on="departmentId", right_on = "id")
    merged_df = merged_df.groupby("name_y").apply(lambda x: x[x["salary"]==x["salary"].max()])
    df = merged_df.reset_index(drop = True)
    # print(df)
    df = df.rename(columns = {"name_y":"Department", "name_x":"Employee", "salary":"Salary"})
    return df[["Department","Employee","Salary"]]