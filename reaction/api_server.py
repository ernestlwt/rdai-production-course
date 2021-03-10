from model import MyModel

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel

from PIL import Image
import io

app = FastAPI()


@app.post("/predict")
async def predict_picture(file: UploadFile = File(...)):

    image = await file.read()

    image = Image.open(io.BytesIO(image))
    prediction = await MyModel().predict.call((image))
    return {"prediction": prediction}

