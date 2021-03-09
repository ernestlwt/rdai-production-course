import asyncio

from model import MyModel

if __name__ == '__main__':
    m = MyModel()

    loop = asyncio.get_event_loop()
    loop.create_task(m.predict.consume())
    loop.run_forever()
