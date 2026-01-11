import pandas as pd
import numpy as np


# ---------- 1. Orders （Helena） ----------
def clean_orders(df_orders: pd.DataFrame) -> pd.DataFrame:
    """
    Clean orders table:
    - drop orders that were never approved
    - convert date columns to datetime
    - (optional) filter invalid statuses, etc.
    """
    df = df_orders.copy()

    # ① delete non-ordered
    df = df[~df["order_approved_at"].isna()].copy()

    # ② change type to datatime
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_timestamp",
        "order_estimated_delivery_date",
    ]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col])

    return df


# ---------- 2. Customers （Alexandra） ----------
def clean_customers(df_customers: pd.DataFrame) -> pd.DataFrame:
    """
    Clean customers table:
    - normalize city / state strings
    - remove duplicates, etc.
    """
    df = df_customers.copy()

    # drop space and lower
    df["customer_city"] = df["customer_city"].str.strip().str.lower()

    # drop space and upper
    df["customer_state"] = df["customer_state"].str.strip().str.upper()

    return df


# ---------- 3. Products （Ghazal） ----------
def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the products table:
    - normalize product_category_name (lowercase, strip, fix spelling)
    - fill missing category names with 'unknown'
    - clean product weight & dimensions (remove 0 and negative values)
    """

    df = df.copy()

    # -------------------------------
    # 1. Clean product_category_name
    # -------------------------------

    # lowercase
    df["product_category_name"] = df["product_category_name"].str.lower()

    # fill missing with "unknown"
    df["product_category_name"] = df["product_category_name"].fillna("unknown")

    # remove extra spaces
    df["product_category_name"] = (
        df["product_category_name"].str.strip().str.replace(r"\s+", " ", regex=True)
    )

    # spelling fixes
    fixes = {
        "costruction_tools_garden": "construction_tools_garden",
        "costruction_tools_tools": "construction_tools_tools",
        "fashio_female_clothing": "fashion_female_clothing",
        "home_confort": "home_comfort",
        "home_comfort_2": "home_comfort",
        "home_appliances_2": "home_appliances",
        "small_appliances": "home_appliances",
        "small_appliances_home_oven_and_coffee": "home_appliances",
        "food_drink": "food_and_drinks",
        "drinks": "food_and_drinks",
        "food": "food_and_drinks",
    }
    df["product_category_name"] = df["product_category_name"].replace(fixes)

    # -------------------------------
    # 2. Clean numeric dimensions
    # -------------------------------
    numeric_cols = [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    for col in numeric_cols:
        # replace zeros with NaN
        df[col] = df[col].replace(0, np.nan)

        # remove negative values
        df.loc[df[col] < 0, col] = np.nan

        # optionally: drop rows with missing dimensions
        # df = df[df[col].notna()]  # optional

    # -------------------------------
    # 3. Return cleaned subset
    # -------------------------------
    cleaned_cols = [
        "product_category_name",
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm",
    ]

    return df


def clean_all(df: pd.DataFrame) -> pd.DataFrame:
    """
    Run all cleaning steps on the merged dataframe.
    """
    df = clean_orders(df)
    df = clean_customers(df)
    df = clean_products(df)
    return df
