from datetime import date
from typing import Dict
import pandas as pd

def load_and_combine_parquet_files(file_list):
    """
    Loads and combines Parquet files into a single DataFrame.

    Args:
        file_list (list): List of file paths to Parquet files.

    Returns:
        pd.DataFrame: Combined DataFrame.
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
            employee_id (str): ID of the employee.
            start_date (date): Start date of the date range (inclusive).
            end_date (date): End date of the date range (inclusive).

        Returns:
            pd.DataFrame: Filtered sales data.
        """

        # Convert "KeyDate" column to datetime for filtering
        sales_data_df["KeyDate"] = pd.to_datetime(sales_data_df["KeyDate"])
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        # Filter data
        filtered_sales = sales_data_df[
            (sales_data_df["KeyEmployee"] == employee_id) &
            (sales_data_df["KeyDate"] >= start_date) &
            (sales_data_df["KeyDate"] <= end_date)
        ]
        return filtered_sales
