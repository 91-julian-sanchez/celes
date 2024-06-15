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
    
class SalesByStoreResponse(BaseModel):
    """
    This model defines the response schema for the `/sales/store/{store_id}` endpoint.
    """
    store: str
    TotalQty: int
    TotalAmount: float
    
class User(BaseModel):
    username: str
    password: str

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "password": "pass",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "password": "pass",
        "disabled": True,
    },
}