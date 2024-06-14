from fastapi import FastAPI
from routers import sales 

app = FastAPI()
app.include_router(sales.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
