import pandas as pd
import datetime as dt

subway_df = pd.read_csv('./Seoul_Subway_Boarding_data/seoul_subway_daily_boarding_2015_2019.csv')
print(subway_df)
print(subway_df.head())
print(subway_df.info())
print(subway_df.describe())
print(subway_df[subway_df.RIDE_PASGR_NUM < 10])

print(subway_df[['RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']].mean())
theday = pd.to_datetime(subway_df.USE_DT, format='%Y%m%d')
subway_df['year'] = theday.dt.year
subway_df['month'] = theday.dt.month
subway_df['day'] = theday.dt.day
wday = {0:'월',1:'화',2:'수',3:'목',4:'금',5:'토',6:'일'}
subway_df['wday'] = theday.dt.dayofweek.map(wday)
# 각 연도별 데이터 프레임 생성
df_2015 = subway_df[subway_df['year'] == 2015]
df_2016 = subway_df[subway_df['year'] == 2016]
df_2017 = subway_df[subway_df['year'] == 2017]
df_2018 = subway_df[subway_df['year'] == 2018]
df_2019 = subway_df[subway_df['year'] == 2019]

# 각 데이터 프레임을 딕셔너리에 저장
dfs = {
    2015: df_2015,
    2016: df_2016,
    2017: df_2017,
    2018: df_2018,
    2019: df_2019
}

# 각 연도별 평균 출력
for year, df in dfs.items():
    print(year)
    print(df[['RIDE_PASGR_NUM', 'ALIGHT_PASGR_NUM']].mean())

#sub_inout = subway_df[['LINE_NUM','SUB_STA_NM','RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']]
sub_inout = subway_df[['RIDE_PASGR_NUM','ALIGHT_PASGR_NUM']]
print(sub_inout-sub_inout.min()) # 각 컬럼의 기준점을 0으로 변경시키는 작업 > 데이터 전처리 방법 중 하나
