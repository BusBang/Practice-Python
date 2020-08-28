#짝수, 홀수인지 판단하기

# 1. 짝수면 True, 홀수면 False
# 2. 홀수면 True, 짝수면 False

# 나머지
# 4라는 숫자로 나누면 ?
# quota : 2 remainder : 0
# 10 나누기 2 ? q : 6, remainder : 0
# 11 나누기 2 ? q : 5, remainder : 1


# 짝수
def isEven(num):
    return num % 2 == 0
# 홀수
def isOdd(num):
    return num % 2 == 1

