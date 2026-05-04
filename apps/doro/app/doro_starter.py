import pandas as pd


df = pd.read_csv('한국도로교통공단_사고유형별 교통사고 통계_20241231.csv', encoding='cp949')

print(df.head(10))