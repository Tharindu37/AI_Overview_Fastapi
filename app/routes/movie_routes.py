from fastapi import APIRouter
from app.models.movie_model import Movie
from app.service.movie_service import predict

router=APIRouter()

@router.post("/predict/")
async def predict_movie_rating(data: Movie):
    predicted_result = await predict(data)
    print(predicted_result) 
    return{
        "predicted_result":float(predicted_result[0][0]) 
    }
    