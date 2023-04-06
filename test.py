import pandas as pd


def Finace_data(code, name):
    # 데이터 얻기
    data = fdr.DataReader(code, start='2022-01-01', end='2022-12-31')
    # 결측지 제거
    data.dropna(inplace=True)
    # csv로 저장
    path = r'C:\ITWILL\3_TextMining'
    data.to_csv(f'{path}/df_{name}_data.csv')

#함수 실행
Finace_data('005930', 'Samsung')