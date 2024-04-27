from fastapi import APIRouter
from app.models.flower_model import Flower
from app.service.flower_service import predict

router=APIRouter()

@router.post("/predict-flower")
def predict_flower(data:Flower):
    predicted_result= predict(data)
    return{
        "predicted_result":str(predicted_result)
    }