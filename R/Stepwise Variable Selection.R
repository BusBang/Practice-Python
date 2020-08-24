##최적회귀방정식

# 1) 데이터 프레임 생성
x1<-c(7, 1, 11, 11, 7, 11, 3, 1, 2, 21, 1, 11, 10)
x2<-c(26, 29, 56, 31, 52, 55, 71, 31, 54, 47, 40, 66, 68)
x3<-c(6, 15, 8, 8, 6, 9, 17, 22, 18, 4, 23, 9, 8)
x4<-c(60, 52, 20, 47, 33, 22, 6, 44, 22, 26, 34, 12, 12)
y<-c(78.5, 74.3, 104.3, 87.6, 95.9, 109.2, 102.7, 72.5, 93.1, 115.9, 83.8, 113.3, 109.4)

df<-data.frame(x1, x2, x3, x4, y)
head(df)

#2) 회귀모형 생성
a <- lm(y~x1+x2+x3+x4, data=df)
summary(a)

#3) 벌점화 전진선택법 step()

step(lm(y~1, data=df), scope=list(lower=~1, upper=~x1+x2+x3+x4), direction="forward")

# 가장 먼저 선택된 변수는 AIC 값이 58.852였던 x4.
# 이어서 x1을 추가하였을 때 28.742, x2를 추가하였을 때 24.974로 최소화된다.

# 벌점화 후진제거법
library(ElemStatLearn)
Data = prostate
data.use = Data[,-ncol(data)]
lm.full.Model = lm(lpsa~., data=data.use)

# 맨 처음 AIC는 -62.67로 gleason을 제거하고 회귀 분석 실시, 그 다음 차례로 lcp, pgg45 순서로 제거되어 회귀분석이 실시된다.