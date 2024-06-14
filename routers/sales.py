from fastapi import APIRouter, HTTPException

from datetime import date
from models import SalesByEmployeeResponse
from services.sales_service import SalesService
import logging  # Import the logging module


logger = logging.getLogger('celes_app')
logger.setLevel(logging.INFO)

router = APIRouter()


@router.get("/sales/employee/{employee_id}", response_model=SalesByEmployeeResponse)
def get_sales_by_employee(employee_id: str, start_date: date, end_date: date):
    """
    This endpoint retrieves sales data for a specific employee within a date range and calculates totals.

    Args:
        employee_id (str): ID of the employee.
        start_date (date): Start date of the date range (inclusive).
        end_date (date): End date of the date range (inclusive).

    Returns:
        SalesByEmployeeResponse: Dictionary containing employee ID, total quantity sold, and total sales amount.

    Raises:
        HTTPException: If an error occurs during data retrieval.
    """

    try:
        logger.info(f"Retrieving sales by employee (KeyEmployee={employee_id}): {start_date} to {end_date}")
        sales = SalesService.get_sales_by_employee(employee_id, start_date, end_date)
        return sales
    except Exception as e:
        logger.error(f"Error: {str(e)}")  # Log the error message with ERROR level
        raise HTTPException(status_code=400, detail=str(e))

