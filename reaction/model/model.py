import os

from reaction.rpc import RabbitRPC
from typing import List

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image

class rpc(RabbitRPC):
    URL = os.environ.get('MQ_SERVER_URL')

class MyModel:
    def __init__(self):
        self.model = ResNet50(weights='imagenet')

    @rpc()
    def predict(self, image):
        image = image.resize((224, 224))
        x = np.asarray(image)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = self.model.predict(x)
        top_pred = decode_predictions(preds, top=1)

        print(str(top_pred), flush=True )

        return [top_pred[0][0][1]]
