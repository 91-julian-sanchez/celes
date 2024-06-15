from fastapi import APIRouter, HTTPException, Depends
from datetime import date
from models import SalesByEmployeeResponse, SalesByProductResponse, SalesByStoreResponse
from services.sales_service import SalesService
import logging



logger = logging.getLogger('celes_app')
logger.setLevel(logging.INFO)

router = APIRouter()

@router.get("/sales/employee/{employee_id}", response_model=SalesByEmployeeResponse)
def get_sales_by_employee(employee_id: str, start_date: date, end_date: date):
    """
    This endpoint retrieves sales data for a specific employee within a date range and calculates totals.

    **Parameters:**

    * **employee_id (str):** The ID of the employee whose sales data you want to retrieve.
    * **start_date (date):** The start date of the date range (inclusive) in YYYY-MM-DD format.
    * **end_date (date):** The end date of the date range (inclusive) in YYYY-MM-DD format.

    **Returns:**

    A `SalesByEmployeeResponse` object containing:

    * **employee (str):** The ID of the employee.
    * **TotalQty (int):** The total quantity of products sold by the employee during the specified date range.
    * **TotalAmount (float):** The total sales amount generated by the employee during the specified date range.

    **Raises:**

    * **HTTPException (status_code=400, detail=str(e)):** If an error occurs during data retrieval.

    **Example usage:**

    ```
    curl -X GET http://your-api-url/sales/employee/123?start_date=2024-06-01&end_date=2024-06-14
    ```
    """

    try:
        logger.info(f"Retrieving sales by employee (KeyEmployee={employee_id}): {start_date} to {end_date}")
        sales = SalesService.get_sales_by_employee(employee_id, start_date, end_date)
        return sales
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/sales/product/{product_id}", response_model=SalesByProductResponse)
def get_sales_by_product(product_id: str, start_date: date, end_date: date):
    """
    This endpoint retrieves sales data for a specific product within a date range and calculates totals.

    **Parameters:**

    * **product_id (str):** The ID of the product whose sales data you want to retrieve.
    * **start_date (date):** The start date of the date range (inclusive) in YYYY-MM-DD format.
    * **end_date (date):** The end date of the date range (inclusive) in YYYY-MM-DD format.

    **Returns:**

    A `SalesByProductResponse` object containing:

    * **product (str):** The ID of the product.
    * **TotalQty (int):** The total quantity of the product sold during the specified date range.
    * **TotalAmount (float):** The total sales amount generated by the product during the specified date range.

    **Raises:**

    * **HTTPException (status_code=400, detail=str(e)):** If an error occurs during data retrieval.

    **Example usage:**

    ```
    curl -X GET http://your-api-url/sales/product/ABC123?start_date=2024-06-01&end_date=2024-06-14
    ```
    """

    try:
        logger.info(f"Retrieving sales by product (KeyProduct={product_id}): {start_date} to {end_date}")
        sales = SalesService.get_sales_by_product(product_id, start_date, end_date)
        return sales
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/sales/store/{store_id}", response_model=SalesByStoreResponse)
def get_sales_by_store(store_id: str, start_date: date, end_date: date):
    """
    This endpoint retrieves sales data for a specific store within a date range and calculates totals.

    **Parameters:**

    * **store_id (str):** The ID of the store whose sales data you want to retrieve.
    * **start_date (date):** The start date of the date range (inclusive) in YYYY-MM-DD format.
    * **end_date (date):** The end date of the date range (inclusive) in YYYY-MM-DD format.

    **Returns:**

    A `SalesByStoreResponse` object containing:

    * **store (str):** The ID of the store.
    * **TotalQty (int):** The total quantity of products sold by the store during the specified date range.
    * **TotalAmount (float):** The total sales amount generated by the store during the specified date range.

    **Raises:**

    * **HTTPException (status_code=400, detail=str(e)):** If an error occurs during data retrieval.

    **Example usage:**

    ```
    curl -X GET http://your-api-url/sales/store/123?start_date=2024-06-01&end_date=2024-06-14
    ```
    """
    try:
        logger.info(f"Retrieving sales by store (KeyStore={store_id}): {start_date} to {end_date}")
        sales = SalesService.get_sales_by_store(store_id, start_date, end_date)
        return sales
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
