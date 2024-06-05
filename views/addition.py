from fastapi import APIRouter, HTTPException
from app.models.request_response_models import AdditionRequestModel, AdditionResponseModel
from app.controllers.addition_controller.py import perform_addition
from datetime import datetime

router = APIRouter()

@router.post("/add", response_model=AdditionResponseModel)
async def add_numbers(request: AdditionRequestModel):
    started_at = datetime.utcnow()
    try:
        result = perform_addition(request.payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    response = AdditionResponseModel(
        batchid=request.batchid,
        response=result,
        status="complete",
        started_at=started_at,
        complete_at=datetime.utcnow()
    )
    return response