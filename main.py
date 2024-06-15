from fastapi import FastAPI
from routers import sales , auth

app = FastAPI()
app.include_router(sales.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
