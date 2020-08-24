##시계열분석

##분해 시계열

#예제 - 영국 왕 42명의 사망 시 나이.
#비계절성을 띄는 시계열자로로서 트렌드 요소, 불규칙 요소로 구성
#20번째 왕까지는 38세~55세의 수명을 유지
#이후 왕은 수명이 늘어서 40번째왕은 73세까지 생존

# 1) 자료 읽기 및 그래프 그리기
library(tseries)
library(forecast)
library(TTR)
king <- scan("http://robjhyndman.com/tsdldata/misc/kings.dat", skip3)
king.ts <- ts(king)
plot.ts(king.ts)

# 2) 3년 마다 평균을 내서 그래프를 부드럽게 표현
king.sma3 <- SMA(king.ts, n=3)
plot.ts(king.sma3)

# 3) 8년 마다 평균을 내서 그래프를 부드럽게 표현
king.sma8 <- SMA(king.ts, n=8)
plot.ts(king.sma8)

##ARIMA 모델 - 정상성 시계열에 한해 사용한다.
#1) 자료 읽기 및 그래프 그리기
king.ff1 <- diff(king.ts, differences=1)
plot.ts(king.ff1)

# 2) ACF와 PACF를 통한 적합한 ARIMA 모델 결정
# 2-1 ACF
acf(king.ff1, lag.max=20)
acf(king.ff1, lag.max=20, plot=FALSE)

## ACF값이 lag 1인 지점 빼고는 모두 점선 구간 안에 있고, 나머지는 구간 안에 있다

# 2-2 PACF
pacf(king.ff1, lag.max=20)
pacf(king.ff1, lag.max=20, plot=FALSE)

## PACF값이 lag 1, 2, 3에서 점선 구간을 초과하고 음의 값을 가지며 절단점이 lag 4이다.

# 3) 적절한 ARIMA모형 찾기
auto.arima(king)

#영국 왕의 사망 나이 데이터의 적절한 ARIMA모형은 ARIMA(0,1,1) 이다

# 4) 예측
king.arima <- arima(king, order=c(0, 1, 1))
king.forecasts <- forecast(king.arima)
king.forecasts

## 42명의 영국왕 중에서 마지막 왕의 사망시 나이는 56세
## 43번째에서 52번째 왕까지 10명의 왕의 사망시 나이를 예측한 결과 67.75살로 추정됨.
## 신뢰 구간은 80%~95%사이