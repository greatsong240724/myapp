import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
file_path = '202406_202406_연령별인구현황_월간.csv'

# 데이터 로드
df = pd.read_csv(file_path, encoding='cp949')

# 스트림릿 앱 설정
st.title('지역별 인구 구조 시각화')
st.sidebar.header('옵션')

# 지역 목록 추출
regions = df['행정구역'].unique()
selected_region = st.sidebar.selectbox('지역을 선택하세요', regions)

# 선택한 지역의 데이터 필터링
region_data = df[df['행정구역'] == selected_region]

# 연령별 인구 데이터만 추출
age_columns = [col for col in df.columns if '세' in col]
age_data = region_data[age_columns].T
age_data.columns = ['인구수']
age_data.index = age_data.index.str.extract('(\d+세)').astype(str)  # '세' 만 추출
age_data.index.name = '연령대'

# 꺾은선 그래프 그리기
fig, ax = plt.subplots()
age_data.plot(kind='line', ax=ax)
ax.set_title(f'{selected_region} 지역의 연령별 인구 구조')
ax.set_xlabel('연령대')
ax.set_ylabel('인구수')
plt.xticks(rotation=45)
st.pyplot(fig)


