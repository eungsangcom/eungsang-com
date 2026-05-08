import json
from pathlib import Path

import pandas as pd

_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "Titanic-Dataset.csv"

class Walter:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv(_CSV_PATH)
        # 인덱스 1번 행만 반환 (DataFrame 형태 유지)
        return df.iloc[[0]].astype(object).where(df.iloc[[0]].notna(), None)

    def get_count(self):
        df = pd.read_csv(_CSV_PATH)
        # 전체 승객 수(전체 행 수) 반환
        return int(len(df))

    def get_survived_count(self):
        df = pd.read_csv(_CSV_PATH)
        count = df["Survived"].value_counts()
        return {
            "total": int(len(df)),
            "survived": int(count.get(1, 0)),
            "dead": int(count.get(0, 0))
        }