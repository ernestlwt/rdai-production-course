import os

from reaction.rpc import RabbitRPC
from typing import List

class rpc(RabbitRPC):
    URL = os.environ.get('MQ_SERVER_URL')

class MyModel:
    @rpc()
    def predict(self, input_text):
        return ["hello world"]
