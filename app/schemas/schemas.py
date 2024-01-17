from pydantic import BaseModel

class ValueResponse(BaseModel):
    key: str
    value: str

class AllValuesResponse(BaseModel):
    values: list[ValueResponse]

class ErrorResponse(BaseModel):
    message: str

class DataRequest(BaseModel):
    data: dict[str, str]