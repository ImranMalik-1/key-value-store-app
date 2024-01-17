from fastapi import FastAPI, HTTPException, Body, Query
from typing import Dict
from datetime import datetime, timedelta

app = FastAPI()

key_value_store = {}


def remove_expired_values():
    current_time = datetime.now()
    expired_keys = [key for key, (value, expiration_time) in key_value_store.items() if expiration_time < current_time]
    for key in expired_keys:
        del key_value_store[key]


@app.get("/values", response_model=Dict[str, str])
def get_all_values():
    remove_expired_values()
    return key_value_store


@app.get("/values/{keys}", response_model=Dict[str, str])
def get_specific_values(keys: str = Query(...)):
    remove_expired_values()
    requested_keys = keys.split(',')
    result = {key: value for key, (value, _) in key_value_store.items() if key in requested_keys}
    return result


@app.post("/values", response_model=dict)
def save_values(data: Dict[str, str] = Body(...)):
    current_time = datetime.now()
    ttl = timedelta(minutes=5)
    
    for key, value in data.items():
        key_value_store[key] = (value, current_time + ttl)
    
    return {"message": "Values stored successfully"}


@app.patch("/values", response_model=dict)
def update_values(data: Dict[str, str] = Body(...)):
    current_time = datetime.now()
    ttl = timedelta(minutes=5)
    
    for key, value in data.items():
        if key in key_value_store:
            key_value_store[key] = (value, current_time + ttl)
        else:
            raise HTTPException(status_code=404, detail=f"Key {key} not found")
    
    return {"message": "Values updated successfully"}
