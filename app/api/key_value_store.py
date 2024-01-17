from fastapi import APIRouter, HTTPException, Path
from datetime import datetime, timedelta
from schemas.schemas import AllValuesResponse, ErrorResponse, DataRequest

key_value_router = APIRouter()

key_value_store = {}

def remove_expired_values():
    """
        __desc__: this function will run everytime to check if a key was expired
                  and remove it from the store
    """
    current_time = datetime.now()
    expired_keys = [key for key, (_, expiration_time) in key_value_store.items() if expiration_time < current_time]
    for key in expired_keys:
        del key_value_store[key]

@key_value_router.get("/values", response_model=AllValuesResponse)
def get_all_values():
    remove_expired_values()
    return {"values": [{"key": key, "value": value} for key, (value, _) in key_value_store.items()]}

@key_value_router.get("/values/{keys}", response_model=AllValuesResponse)
def get_specific_values(keys: str = Path(...)):
    remove_expired_values()
    requested_keys = keys.split(',')
    result = [{"key": key, "value": value} for key, (value, _) in key_value_store.items() if key in requested_keys]
    return {"values": result}

@key_value_router.post("/values", response_model=ErrorResponse)
def save_values(data: DataRequest):
    current_time = datetime.now()
    ttl = timedelta(minutes=5)

    for key, value in data.data.items():
        key_value_store[key] = (value, current_time + ttl)

    return {"message": "Values stored successfully"}

@key_value_router.patch("/values", response_model=ErrorResponse)
def update_values(data: DataRequest):
    current_time = datetime.now()
    ttl = timedelta(minutes=5)

    for key, value in data.data.items():
        if key in key_value_store:
            key_value_store[key] = (value, current_time + ttl)
        else:
            raise HTTPException(status_code=404, detail=f"Key {key} not found")

    return {"message": "Values updated successfully"}
