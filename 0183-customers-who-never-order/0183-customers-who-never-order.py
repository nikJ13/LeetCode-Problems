import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = customers.merge(orders, how="left", left_on="id", right_on="customerId")
    mask = merged_df["customerId"].isna()
    result_df = merged_df[mask]
    return result_df[["name"]].rename(columns={"name":"Customers"})