import numpy as np
from tensorflow.keras.models import load_model
from app.utils.flower_utils import FlowerPath
from app.models.flower_model import Flower

# Class mapping
class_mapping = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# load model
model=load_model(f"{FlowerPath.MODEL_PATH}/iris-model-v01.h5")

def predict(data:Flower):
  # Convert input data to numpy array
  input_data=np.array([data.sepalLength,data.sepalWidth,data.petalLength, data.petalWidth])
  # Reshape
  input_data=input_data.reshape(1,-1)
  # Predict
  predicted_target=model.predict(input_data)
  # Get the index of the maximum value
  max_index = np.argmax(predicted_target)
  # Get the relevant class
  relevant_class = class_mapping[max_index]
  print("Predicted class:", relevant_class)
  return relevant_class