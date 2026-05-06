import pandas as pd

class Reader:
    def __init__(self):
        pass

    def get_data(self):
        df = pd.read_csv('한국도로교통공단_사고유형별 교통사고 통계_20241231.csv', encoding='cp949')
        print(df.head(10))