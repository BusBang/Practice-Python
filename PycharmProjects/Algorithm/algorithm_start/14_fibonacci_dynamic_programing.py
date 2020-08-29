# 피보나치 수열 (다이내믹 프로그래밍)
#   Dynamic programming 동적 프로그래밍

# 메모이제이션 (Memoizaition)
#   함수 호출한 결과값을 메모한다
#   함수 호출은 비용이 크다
#   함수 호출을 적게하기 위한 방법
#   메모해 놓은 값을 넘겨서 이미 계산한 값을 계산하지 않도록 함 (주로 파이썬에선 리스트)
#   메모해둔 값에서 먼저 찾아본다 !!

def fib(n, lookup):
    if n <= 1:
        return n

    # lookup[n]이 없을 때, None일 때 계산해서 넣는 로직
    if lookup[n] is None :
        lookup[n] = fib(n-2, lookup) + fib(n-1, lookup)

    return lookup[n]

n = 100
lookup = [None] * (n + 1) # error 처리. 초기화를 하지 않으면 인덱스에의 접근을 할 수 없다
print(fib(n, lookup))