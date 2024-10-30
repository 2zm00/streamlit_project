import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import yfinance as yf




def bitcoin():
	st.header("비트코인 데이터 예측")

	#비트코인 데이터 가져오기
	btc = yf.download('BTC-USD')

	#타겟 설정
	btc['Target'] = (btc['Close'].shift(-1) > btc['Close']).astype(int)
	btc_df = btc.dropna()

	#특성과 타겟 분리
	X = btc_df[['Open', 'High', 'Low', 'Close', 'Volume']]
	y = btc_df['Target']

	# 학습 데이터와 테스트 데이터 분리
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

	if st.button("비트코인 가격 예측하기", use_container_width=True):
		with st.spinner('예측 모델 학습 중...'):
			
			#모델 학습
			classifier=RandomForestClassifier(n_estimators=100, random_state=42)
			classifier.fit(X_train, y_train)


			#예측
			y_pred = classifier.predict(X_test)
			y_pred_proba = classifier.predict_proba(X_test)

			#정확도 수행
			accuracy = accuracy_score(y_test, y_pred)

			# 결과 표시
			st.metric("모델 정확도", f"{accuracy:.2%}")


			# 분류 보고서
			st.subheader("분류 성능 보고서")
			report = classification_report(y_test, y_pred, output_dict=True)

			st.dataframe(pd.DataFrame(report).transpose())

			# 예측 결과 시각화
			fig, ax = plt.subplots(figsize=(15, 10))

			# 가격 추이
			ax.plot(btc['Close'].tail(100), label='Bitcoin Price', color='blue')


			# 매수 신호 (상승 예측)
			btc_date= btc.index[-len(y_test):]
			buy_signals = btc_date[y_pred==1]
			sell_signals = btc_date[y_pred == 0]

			if len(buy_signals) > 0:
				ax.scatter(buy_signals, btc.loc[buy_signals, 'Close'], color='green', marker='^', label='Buy signal')
			if len(sell_signals) > 0:
				ax.scatter(sell_signals, btc.loc[sell_signals, 'Close'], color='red', marker='v', label='Sell signal')

			plt.title('Bitcoin Predict')
			plt.xlabel('Date')
			plt.ylabel('Price')
			plt.legend()
			st.pyplot(fig)

			# 다음날 예측을 위한 마지막 데이터
			last_data = X.iloc[-1:]
			next_pred = classifier.predict(last_data)[0]
			next_prob = classifier.predict_proba(last_data)[0]

			# 현재 시점 기준 데이터
			current_price = btc['Close'].iloc[-1]
			current_date = btc.index[-1]

			# 결과 데이터프레임 생성
			prediction_df = pd.DataFrame({
				'예측 방향': ['상승' if next_pred == 1 else '하락'],
				'현재 가격': [current_price],
				'예측 확률': [next_prob.max()],
				'예측 시점': [current_date]
			})

			arrow_df = pd.DataFrame(['상승' if next_pred == 1 else '하락'])


			
			# 결과 표시
			st.subheader("예측 결과")
			st.header(arrow_df)
			st.dataframe(prediction_df)



if __name__ == '__main__':
    bitcoin()