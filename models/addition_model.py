from pydantic import BaseModel, Field
from typing import List

class AdditionRequest(BaseModel):
    lists: List[List[int]] = Field(..., example=[[1, 2, 3], [4, 5, 6]])

class AdditionResponse(BaseModel):
    result: List[int]