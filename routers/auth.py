from fastapi import HTTPException, Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional
from models import fake_users_db
from constants.app_constants import SECRET_KEY, ALGORITHM

def authenticate(token: str):
    """
    Function to authenticate the JWT token.

    Args:
    - token (str): JWT token extracted from the Authorization header.

    Returns:
    - str: Token if it's valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
    return token

def get_current_user(token: str = Depends(authenticate)):
    """
    Function to extract and validate the JWT token from the Authorization header.

    Args:
    - token (str): JWT token extracted from the Authorization header.

    Returns:
    - dict: Dictionary containing the user information if the token is valid.

    Raises:
    - HTTPException: If the token is invalid or expired.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=400, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = fake_users_db.get(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
