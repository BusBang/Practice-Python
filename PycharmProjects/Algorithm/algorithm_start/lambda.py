# lambda 인자 : 표현식
# 함수를 한줄로 만들어준 훌륭한 녀석

def hap(x, y):
    return x+y
# 두 숫자를 더해주는 함수 hap
print(hap(10, 20))

# 람다식으로 표현하면
# (lambda x,y:x+y)(10, 20)
b=(lambda x,y:x+y)(10,20)
print(b)


# map(함수, 리스트)
# map 함수는 함수와 리스트를 인자로 받는다. 그리고 리스트로부터 원소를 하나씩 꺼내어 함수를 적용, 그 결과를 새로운 리스트에 담아준다.
# map 함수를 쓰기 전 list를 사용해준다 -> 파이썬 3

a = list(map(lambda x: x**2, range(5))) #[0,1,2,3,4]
print(a)

# reduce 함수
# reduce(함수, 순서형자료)
# reduce는 함수를 누적해서 적용한다.
from functools import reduce
print(reduce(lambda x, y : x+y, [0,1,2,3,4]))
print(reduce(lambda x, y : x+y, ['a','b','c','d','e']))

# filter()
# fiter(함수, 리스트)
# 리스트에 있는 원소를 함수에 적용시켜 결과가 참인 값들로 새로운 리스트를 만들어줌
print(list(filter(lambda x: x<5, range(10)))) # x<5를 만족하는 필터링.
print(list(filter(lambda x: x%2, range(10)))) # 홀수를 만족하는 필터링. 참은 1, 거짓은0이기 때문.
