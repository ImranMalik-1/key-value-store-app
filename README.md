# FastAPI Key-Value Store

## 1. What the API Does

The FastAPI Key-Value Store is a simple RESTful API that allows users to store and retrieve key-value pairs with a time-to-live (TTL) feature. The key-value pairs can be of arbitrary length, and values are automatically removed from the store after a specified TTL (e.g., 5 minutes). The API supports operations such as storing values, fetching all values, fetching specific values by keys, and updating values with TTL reset.

### Endpoints:

- **GET /values:** Retrieve all values from the store.

   Response example:
   ```json
   {"key1": "value1", "key2": "value2", "key3": "value3", ...}

## Stack
Framework: FastAPI
Language: Python
Containerization: Docker

## The API documentation (Swagger UI) is available at http://localhost:8000/docs.
![Capture](https://github.com/ImranMalik-1/key-value-store-app/assets/54236357/2908b5ea-69be-4edd-becf-7b144dd35788)

