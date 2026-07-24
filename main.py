from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import products, users, user

app = FastAPI(title= "FastAPI-MLZ")

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(user.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola Mundo Lenin with FastAPI..."