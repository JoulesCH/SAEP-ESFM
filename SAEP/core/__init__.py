from fastapi import FastAPI


app = FastAPI()

from endpoints import api_router

app.include_router(api_router, prefix="/api")
