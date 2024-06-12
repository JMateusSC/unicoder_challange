from fastapi import FastAPI
import uvicorn
from routers import user, products

app = FastAPI()

app.include_router(user.router)
app.include_router(products.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)