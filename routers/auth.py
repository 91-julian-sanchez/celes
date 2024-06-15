from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from services.auth_service import create_access_token, authenticate_user
from constants.app_constants import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()

@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para obtener un token de acceso mediante autenticación OAuth2.

    **Parameters:**
    *    **form_data (OAuth2PasswordRequestForm):** Datos del formulario OAuth2 que incluyen
                                               el nombre de usuario y la contraseña.

    **Returns:**
    *    **dict:** Un diccionario que contiene el token de acceso y el tipo de token.

    **Raises:**
    *    **HTTPException:** Si el nombre de usuario o la contraseña son incorrectos.
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


