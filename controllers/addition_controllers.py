from fastapi import APIRouter, HTTPException
from app.models.addition_model import AdditionRequest, AdditionResponse
from app.services.addition_service.py import add_lists

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add(request: AdditionRequest):
    try:
        result = add_lists(request.lists)
        return AdditionResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")
