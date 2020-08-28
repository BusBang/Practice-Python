# StringTokenizer 만들기

## 토큰(Token) 이란?
#   프로그램에서 다루는 최소 단위
#   이름 김경록을 다룰 때 김은 성, 경록은 이름.
#   이 각각을 토큰이라고 함.

## Tokenizer란?
#   가장 작은 단위로 나누어 주는 일을 하는 것.

## StringTokenizer?
#   스트링을 나눠주는 로직

# str = "1+2*(3-4)"
# first = 3 - 4   # -1
# second = 2 * -1 # -2
# third = 1+(-2)  # -1

# 1 + (2 * 3) - (2 * 4)
# 숫자와 괄호를 분리해주는 식

str = "13+{24*(35-46.76)-89}"
# ["13", "+", "24", "*", "(", "35", "-" 46.76", ")"]

#delimiter : 구분자
def stringTokenizer(str, deli):
    result = []
    accu = ""
    for ch in str:
        if ch in deli:
            if accu != "":
                result.append(accu)
                accu = ""
            result.append(ch)   # array에 차례대로 put
        else:
            accu += ch
    return result

print(stringTokenizer(str, "+-*%(){}[]^"))