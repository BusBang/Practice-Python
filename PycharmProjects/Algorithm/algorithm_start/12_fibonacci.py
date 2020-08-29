# 피보나치 수열
#   1, 1, 2, 3, 5, 8
#   앞 숫자가 있어야 뒤에 것을 구할 수 있다.
#   fib(n) = fib(n-1) + fib(n-2)
#   fib(6)을 구하려면 fib(5)와 fib(4)를 알아야 한다.

#   fib(1) = 1  [1]
#   fib(2) = 1  [1, 1]
#   fib(3) = 2  [1, 1, 2]
#   fib(4) = 3  [1, 1, 2, 3]
#   fib(5) = 5  [1, 1, 2, 5]
#   fib(6) = 8  [1, 1, 2, 5, 8]

def fib(num):
    result = []
    first = 1
    second = 1
    if num > 1:
        result.append(first)

    result.append(second)
    for i in range(2, num):
        third = first + second
        result.append(third)
        first = second
        second = third
    return result.pop()

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(7))
