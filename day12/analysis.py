import pandas as pd

# 데이터 불러오기
sales_df = pd.read_csv("data/파일명.csv", encoding="cp949")

# 1. 커피-음료 업종 필터링
filtered_df = sales_df[
    sales_df['서비스_업종_코드_명'] == '커피-음료'
]

# 2. 상권별 토요일 매출 합계
grouped = filtered_df.groupby('상권_코드_명')['토요일_매출_금액'].sum().reset_index()

# 3. 매출 높은 순 정렬
grouped = grouped.sort_values(by='토요일_매출_금액', ascending=False)

# 4. 상위 10개 출력
top10 = grouped.head(10)

print(top10)