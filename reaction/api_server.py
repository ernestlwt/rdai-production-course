from model import MyModel

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Comment(BaseModel):
    text: str

@app.post("/predict")
async def predict_comment(comment:Comment):
    prediction = await MyModel().predict.call((comment.text))
    return {"prediction": prediction}

