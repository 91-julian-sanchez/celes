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
            employee_id (str): ID of the employee.
            start_date (date): Start date of the date range (inclusive).
            end_date (date): End date of the date range (inclusive).

        Returns:
            Dict: Dictionary containing employee ID, total quantity sold, and total sales amount.
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
