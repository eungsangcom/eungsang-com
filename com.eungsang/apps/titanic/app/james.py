from fastapi import FastAPI

try:
    from titanic.app.walter import Walter
except ModuleNotFoundError:
    from apps.titanic.app.walter import Walter

try:
    from titanic.app.roze import Roze, _MODEL_PATH
except ModuleNotFoundError:
    from apps.titanic.app.roze import Roze, _MODEL_PATH

app = FastAPI(title="Titanic (James)")


class James:
    def __init__(self):
        pass


    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()

    def get_survived_count(self):
        w = Walter()
        return w.get_survived_count()

    def check_decision_tree_model(self):
        r = Roze()
        model_path = _MODEL_PATH
        return {
            "exists": bool(model_path.exists()),
            "model_path": str(model_path),
            "message": "결정트리 모델이 존재합니다."
            if model_path.exists()
            else "결정트리 모델이 없습니다. 먼저 save_decision_tree_model()을 실행하세요.",
        }