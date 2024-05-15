from fastapi import APIRouter, UploadFile, File
from app.service.cat_and_dog_service import predict

router=APIRouter()

@router.post("/predict-car-or-dog")
async def predict_cat_or_dog(file: UploadFile=File(...)):
    predicted_result=await predict(file)
    return{
        "predicted_result":(predicted_result)
    }