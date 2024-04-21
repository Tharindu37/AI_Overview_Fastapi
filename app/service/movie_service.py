import numpy as np
import joblib
from app.models.movie_model import Movie
from app.utils.movie_utils import MoviePath
from tensorflow.keras.models import load_model

# Load your scaler and model
scaler_data = joblib.load(f"{MoviePath.MODEL_PATH}/scaler_data.pkl")
scaler_target = joblib.load(f"{MoviePath.MODEL_PATH}/scaler_target.pkl")
model = load_model(f"{MoviePath.MODEL_PATH}/model.h5")
# model =joblib.load(f"{MoviePath.MODEL_PATH}/model.pkl")

async def predict(data: Movie):
    # Convert input data to numpy array
    input_data = np.array([data.year, data.time, data.votes])
    # Scale input data
    scaled_data = scaler_data.transform([input_data])
    # Predict
    result = model.predict(scaled_data)
    # Inverse transform predicted result
    predicted_result = scaler_target.inverse_transform(result)
    return predicted_result