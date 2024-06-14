from datetime import date
from typing import Dict
import pandas as pd


def load_and_combine_parquet_files(file_list: list) -> pd.DataFrame:
    """
    Loads and combines multiple Parquet files into a single pandas DataFrame.

    Args:
        file_list (list): A list of file paths pointing to the Parquet files to be combined.

    Returns:
        pd.DataFrame: The combined DataFrame containing data from all the Parquet files.

    Assumptions:
        * All Parquet files in the `file_list` have the same schema (column names and data types).
    """

    dataframes = [pd.read_parquet(file) for file in file_list]
    combined_df = pd.concat(dataframes, ignore_index=True)
    return combined_df


files = [
    "./data/data_chunk000000000000.snappy.parquet",
    "./data/data_chunk000000000001.snappy.parquet",
    "./data/data_chunk000000000002.snappy.parquet",
    "./data/data_chunk000000000003.snappy.parquet"
]

# Load and combine all Parquet files into one
sales_data_df = load_and_combine_parquet_files(files)


class SalesRepository:
    @staticmethod
    def get_sales_by_employee(employee_id: str, start_date: date, end_date: date) -> pd.DataFrame:
        """
        Gets sales data for a specific employee within a date range.

        Args:
            employee_id (str): ID of the employee whose sales data to retrieve.
            start_date (date): Start date of the date range (inclusive) in YYYY-MM-DD format.
            end_date (date): End date of the date range (inclusive) in YYYY-MM-DD format.

        Returns:
            pd.DataFrame: A DataFrame containing filtered sales data for the specified employee and date range.

        Assumptions:
            * The `sales_data_df` (assumed to be loaded from Parquet files) has columns named
              "KeyEmployee", "KeyDate", and potentially other sales-related columns.
            * The "KeyDate" column is in a format compatible with pandas datetime conversion.
        """

        sales_data_df["KeyDate"] = pd.to_datetime(sales_data_df["KeyDate"])
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_sales = sales_data_df[
            (sales_data_df["KeyEmployee"] == employee_id) &
            (sales_data_df["KeyDate"] >= start_date) &
            (sales_data_df["KeyDate"] <= end_date)
        ]
        return filtered_sales

    @staticmethod
    def get_sales_by_product(product_id: str, start_date: date, end_date: date) -> pd.DataFrame:
        """
        Gets sales data for a specific product within a date range.

        Args:
            product_id (str): ID of the product whose sales data to retrieve.
            start_date (date): Start date of the date range (inclusive) in YYYY-MM-DD format.
            end_date (date): End date of the date range (inclusive) in YYYY-MM-DD format.

        Returns:
            pd.DataFrame: A DataFrame containing filtered sales data for the specified product and date range.

        Assumptions:
            * Same assumptions as `get_sales_by_employee` regarding `sales_data_df` and "KeyDate" column.
        """

        sales_data_df["KeyDate"] = pd.to_datetime(sales_data_df["KeyDate"])
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        filtered_sales = sales_data_df[
            (sales_data_df["KeyProduct"] == product_id) &
            (sales_data_df["KeyDate"] >= start_date) &
            (sales_data_df["KeyDate"] <= end_date)
        ]
        return filtered_sales
