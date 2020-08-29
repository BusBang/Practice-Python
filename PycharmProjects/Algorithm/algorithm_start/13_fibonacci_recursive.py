# 피보나치 수열 (재귀)
#   1, 1, 2, 3, 5, 8
#   재귀는 거꾸로 생각해야 한다.
#   fib(n) = fib(n-1) + fib(n-2)
#   fib(6)을 구하려면 fib(5)와 fib(4)를 알아야 한다.

#   fib(1) = 1
#   fib(2) = 1
#   fib(3) = 2
#   fib(4) = 3
#   fib(5) = 5
#   fib(6) = 8

def fib(n):
    if n <= 1:
        return n
    return fib(n-2) + fib(n-1)

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))

# print(fib(1000)) - 재귀함수는 매우 느리다.

# fib(6) = fib(5) + fib(4) = 5 + 3 = 8
# fib(5) = fib(4) + fib(3) = 3 + 2 = 5
# fib(4) = fib(3) + fib(2) = 2 + 1 = 3
# fib(3) = fib(2) + fib(1) = 1 + 1 = 2
# fib(2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(1) = 1
# fib(0) = 0