#파이썬 내장 함수
#   -파이썬 인터프리터가 제공하는 함수
#   -사용법을 알아두면 개발 속도 및 안정성 향상
#   -종류 : 문자열 관련 함수, 수학 관련 함수

##1. 문자열 관련 함수

#1) 문자 개수 세기 : count()
'hello'.count('l')
#   2

#2) 전체 문자열 내 특정 문자열 위치 알려주기 : find(),index()
#   둘 다 찾는 문자열이 처음 나타는 위치 반환.
#   없으면 find()는 -1반환, index()는 error 발생
'hello'.find('l')
#   2
'hello'.find('i')
#   -1
'hello'.index('l')
#   2
# 'hello'.index('i')
#   ValueError : substring not found

#3) 문자열 삽입 : join()
#   인수로 받은 문자열의 문자들 사이사이마다 앞의 문자열을 삽입
'-'.join('hello')
#   'h-e-l-l-o'

#4) 문자열 나누기 : split()
#   문자열을 인수로 받은 문자열을 기준으로 나누어 리스트의 원소로 만들어줌
'h-e-l-l-o'.split('-')
print('h-e-l-l-o'.split('-'))
#   ['h', 'e', 'l', 'l', 'o']

#5) 문자열 검사
#   isdigit()   :   문자열이 숫자로만 되어있을 때 True
a = '293123'.isdigit()
print(a)

#   isalpha()   :   문자열이 알파벳이나 한글문자로 되어있을 때 True
a = 'abdㄱㄴㄷ'.isalnum()
print(a)

#   isalnum()   :   문자열이 숫자, 영문자, 한글문자만 섞여있을 때 True
a = '293fncㄱㄴㄷ'.isalnum()
print(a)

#   isupper()   :   문자열이 대문자로 되어있을 때 True
a = '293ABC'.isupper()
print(a)

#   islower()   :   문자열이 소문자로 되어있을 때 True
a = '293fnc'.islower()
print(a)

#6) 문자열 변환
#   upper()     :   문자열을 모두 대문자로 변환
a = 'asdfzxcv0'.upper()
print(a)
#   lower()     :   문자열을 모두 소문자로 변환
a = 'ASDFQWER334'.lower()
print(a)

#   replace(old, new[,count])
#   -old 문자열을 모두 new문자열로 반환.
#   -count 옵션이 설정되어 있으면, count번깨까지 발견한 old 문자열만 반환
a = 'asdfqwerasdf123wdasxc'.replace('a',' ')
print(a)

#2. 수학 관련 함수
#1) 수치 계산을 위한 함수
#   max(a,b,c, ...)     :   두 개 이상의 인수를 주면 그 중 최댓값을 반환
a = max(1,2,3)
print(a)
#   min(a,b,c, ...)     :   두 개 이상의 인수를 주면 그 중 최솟값을 반환
a = min(1,2,3)
print(a)
#   abs(a)     :   a의 절댓값을 반환
a = abs(-5)
print(a)
#   sum(x[, start=0])     :   x는 리스트 드으이 반복되는 데이터이며 총합을 반환. start 값이 지정되면 start 수치도 더해서 반환
a = sum([1,2,3])
print(a)
a = sum([1,2,3],2)
print(a)
#   pow(x,y[,z])     :   z가 없으면 x^y를 반환하고, z가 있으면 x^y%z를 반환
a = pow(2,3)
print(a)
a = pow(2,3,5)
print(a)
#   round(x)    :   반올림하여 정수를 반환
a = round(1.2)
print(a)

#2) math 모듈 내 수학 함수
#   - 함수 사용 전 먼저 import math 수행
#   - 호출 시 함수 이름 앞에 math. 을 붙여줌
import math

#   log(x[, base])  :   x의 로그를 반환. base가 생략되면 자연로그, 지정되면 base값을 밑으로 하는 로그 값을 반환
print(math.log(4))
#   sqrt(x)     :   x의 제곱근을 반환
print(math.log(4,2))
#   sin(x), cos(x), tan(x)  : x는 라디안 각도. 각 삼각함수를 계산하여 반환
print(math.sqrt(9))
#   radians(x)  :   degree 각도를 넣어주면 라디안 각도를 반환
print(math.sin(math.radians(90)))
#   pi  :   원주율 값을 가진 상수
print(math.pi)
#   어림함수
#   ceil(x)     :   x보다 크거나 같은 최소의 정수로 어림함
print(math.ceil(4.2))
#   floor(x)     :   x보다 작거나 같은 최대의 정수로 어림함
print(math.floor(4.2))
#   trunc(x)     :   소수점 아래 값을 버림
print(math.trunc(4.2))
