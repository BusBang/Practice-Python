# 모듈
#   -자주 쓰는 기능들을 하나로 묶은 것.
#   - .py 로 되어있는 파일
#   -자주 쓰는 기능은 주로 함수들로 구현되므로 모듈은 "함수들을 하나로 묶은 것"으로 볼 수 있음

# 모듈의 장점
#   - 코드 재사용에 의한 개발 속도 증대
#   - 코드가 간결해진다

# 모듈의 작성 및 사용 (계산기)
# 모듈 작성
#   - 더하기, 빼기, 곱하기, 나누기 함수 정의
#   calculator.py
# def sum(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def mul(a,b):
#     return a*b
#
# def div(a,b):
#     return a/b

# 모듈 사용
# (1) 모듈 import 하기
#   import 모듈명
#   import calculator
# (2) 모듈 내 함수 사용하기
#   모듈명.모듈 내 함수
#   import caculator.py (py 생략 가능능)
#   print(calculator.sum(1, 2))
#   3 출력

# 모듈 불러오기 옵션
#   (1) 원하는 함수만 import 하기 (이렇게 불러온 경우, 함수 호출 시 모듈명 생략)
#   from 모듈이름 import 모듈에 포함된 함수1, 함수2
#   from calculator import sum
#   sum(3,4)
#   7 출력
#   (2) 특정 모듈 내 모든 함수를 불러오기 (모듈 명을 생략할 수 있는 장점이 있다.)
#   from calculator import *

# 모듈 사용시 유의사항
# (1) 모듈 경로 지정하기
#   -모듈과 실행하는 파일은 같은 곳에 있거나 모듈의 위치를 명확히 지정해야함. (기본적으론 같은 경로 파일만 가능)
#   - set 명령어
#   set PYTHONPATH=(경로)
#   set PYTHONPATH=C:\Python\calculator.py
