import numpy as np
from tensorflow.keras.models import load_model
from app.utils.cat_and_dog_utils import CatAndDogPath
from fastapi import File, UploadFile
import cv2

#Load model
model=load_model(f"{CatAndDogPath.MODEL_PATH}")
category_dict = {0: 'Dog', 1: 'Cat'}

async def predict(file: UploadFile = File(...)):
    print("okk")
    try:
        # Read the uploaded file
        contents= await file.read()

        # Convert the file content to an OpenCV image
        nparr= np.frombuffer(contents, np.uint8)
        img=cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Preprocess the image
        test_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        test_img = cv2.resize(test_img, (50, 50))
        test_img = test_img / 255.0
        test_img = test_img.reshape(1, 50, 50, 1)

        # Perform prediction
        result = model.predict(test_img)
        label = np.argmax(result, axis=1)[0]
        category = category_dict[label]
        return str(category)
    except Exception as e:
        return str(e)