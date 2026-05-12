from fastapi import FastAPI

try:
    from doro.app.doro_reader import Reader
except ModuleNotFoundError:
    from apps.doro.app.doro_reader import Reader

app = FastAPI(title="Doro (doro_derector)")


class Director:
    def __init__(self):
        pass


    def get_data(self):
        r = Reader()
        return r.get_data()