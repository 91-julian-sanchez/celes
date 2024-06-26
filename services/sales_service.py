from datetime import date
from typing import Dict
import pandas as pd

from repositories.sales_repository import SalesRepository


class SalesService:
    """
    This class provides methods to access and process sales data.
    """

    @staticmethod
    def get_sales_by_employee(employee_id: str, start_date: date, end_date: date) -> Dict:
        """
        Gets sales data for a specific employee within a date range and calculates totals.

        Args:
            employee_id (str): ID of the employee whose sales data to retrieve.
            start_date (date): Start date of the date range (inclusive) in YYYY-MM-DD format.
            end_date (date): End date of the date range (inclusive) in YYYY-MM-DD format.

        Returns:
            Dict: A dictionary containing the following keys:
                * employee (str): The ID of the employee.
                * TotalQty (int): The total quantity of products sold by the employee during the specified date range.
                * TotalAmount (float): The total sales amount generated by the employee during the specified date range.
        """

        # Use SalesRepository to retrieve filtered sales data
        sales_df = SalesRepository.get_sales_by_employee(employee_id, start_date, end_date)

        # Calculate total quantity and total sales amount
        total_qty = sales_df["Qty"].sum()
        total_amount = sales_df["Amount"].sum()

        # Return a dictionary with employee ID, total quantity, and total amount
        return {
            "employee": employee_id,
            "TotalQty": total_qty,
            "TotalAmount": total_amount
        }

    @staticmethod
    def get_sales_by_product(product_id: str, start_date: date, end_date: date) -> Dict:
        """
        Gets sales data for a specific product within a date range and calculates totals.

        Args:
            product_id (str): ID of the product whose sales data to retrieve.
            start_date (date): Start date of the date range (inclusive) in YYYY-MM-DD format.
            end_date (date): End date of the date range (inclusive) in YYYY-MM-DD format.

        Returns:
            Dict: A dictionary containing the following keys:
                * product (str): The ID of the product.
                * TotalQty (int): The total quantity of the product sold during the specified date range.
                * TotalAmount (float): The total sales amount generated by the product during the specified date range.
        """

        sales_df = SalesRepository.get_sales_by_product(product_id, start_date, end_date)
        total_qty = sales_df["Qty"].sum()
        total_amount = sales_df["Amount"].sum()
        return {
            "product": product_id,
            "TotalQty": total_qty,
            "TotalAmount": total_amount
        }

    @staticmethod
    def get_sales_by_store(store_id: str, start_date: date, end_date: date) -> Dict:
        """
        Gets sales data for a specific store within a date range and calculates totals.

        Args:
            store_id (str): ID of the store whose sales data to retrieve.
            start_date (date): Start date of the date range (inclusive) in YYYY-MM-DD format.
            end_date (date): End date of the date range (inclusive) in YYYY-MM-DD format.

        Returns:
            Dict: A dictionary containing the following keys:
                * store (str): The ID of the store.
                * TotalQty (int): The total quantity of products sold by the store during the specified date range.
                * TotalAmount (float): The total sales amount generated by the store during the specified date range.
        """

        sales_df = SalesRepository.get_sales_by_store(store_id, start_date, end_date)
        total_qty = sales_df["Qty"].sum()
        total_amount = sales_df["Amount"].sum()
        return {
            "store": store_id,
            "TotalQty": total_qty,
            "TotalAmount": total_amount
        }