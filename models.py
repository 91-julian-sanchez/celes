from pydantic import BaseModel

class SalesByEmployeeResponse(BaseModel):
    """
    This model defines the response schema for the `/sales/employee/{employee_id}` endpoint.
    """
    employee: str
    TotalQty: int
    TotalAmount: float
    
class SalesByProductResponse(BaseModel):
    """
    This model defines the response schema for the `/sales/product/{product_id}` endpoint.
    """
    product: str
    TotalQty: int
    TotalAmount: float