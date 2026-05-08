import pickle
from pathlib import Path

import pandas as pd

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"
_MODEL_PATH = _DATA_DIR / "titanic_decision_tree.pkl"


class Roze:
    def __init__(self):
        pass

    def save_decision_tree_model(self, model_path: Path | None = None):
        try:
            from sklearn.tree import DecisionTreeClassifier
        except ModuleNotFoundError as exc:
            raise ModuleNotFoundError(
                "scikit-learn이 설치되어 있지 않습니다. `pip install scikit-learn` 후 다시 실행해주세요."
            ) from exc

        df = pd.read_csv(_CSV_PATH)
        if "Survived" not in df.columns:
            raise ValueError("Titanic 데이터셋에 'Survived' 컬럼이 없습니다.")

        y = df["Survived"]
        x = df.drop(columns=["Survived"])

        # 문자열/범주형 컬럼을 원-핫 인코딩 후 결측치는 0으로 채움
        x = pd.get_dummies(x, drop_first=False)
        x = x.fillna(0)

        model = DecisionTreeClassifier(random_state=42)
        model.fit(x, y)

        target_path = Path(model_path) if model_path else _MODEL_PATH
        with open(target_path, "wb") as f:
            pickle.dump(model, f)

        return {
            "message": "결정트리 모델 저장 완료",
            "model_path": str(target_path),
            "rows": int(len(df)),
            "feature_count": int(x.shape[1]),
        }