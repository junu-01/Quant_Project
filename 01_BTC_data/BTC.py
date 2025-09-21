import pandas as pd
import mplfinance as mpf

# 데이터 불러오기
data = pd.read_csv('BTC_data.csv',index_col='Date',parse_dates=True)

# 데이터 전처리 [1]Volume에서 K를 1000으로 변환/숫자타입으로 변환 [2]쉼표(,)제거/숫자타입으로 변환
data['Volume'] = data['Volume'].astype(str).str.replace('K', '').astype(float) * 1000
data['Close'] = data['Close'].astype(str).str.replace(',', '').astype(float)
data['Open'] = data['Open'].astype(str).str.replace(',', '').astype(float)
data['High'] = data['High'].astype(str).str.replace(',', '').astype(float)
data['Low'] = data['Low'].astype(str).str.replace(',', '').astype(float)


# 이동평균선 코드구현
# 종가를 기준으로 5일, 20일 이동평균선을 계산해서 새로운 컬럼으로 추가
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# 이동평균선이 잘 계산되었는지 마지막 5줄을 다시 화면에 출력해서 확인
print(data.tail(5))

# 차트 그리기
# 최근 180일간의 데이터만 잘라서 그릴거다.
recent_data = data.tail(180)

# 차트 그리기
mpf.plot(recent_data, 
         type='candle',          # 캔들 차트
         mav=(5, 20),            # 5일, 20일 이동평균선
         volume=True,            # 거래량 차트
         title='BTC/USDT Daily Chart',
         style='binance')          # 차트 스타일