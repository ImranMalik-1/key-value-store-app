from fastapi import FastAPI
from api.key_value_store import key_value_router

app = FastAPI()

app.include_router(key_value_router)
