import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    res = merged_df[merged_df["customerId"].isnull()]["name"].to_frame(name="Customers")
    return res
    # print(res)es