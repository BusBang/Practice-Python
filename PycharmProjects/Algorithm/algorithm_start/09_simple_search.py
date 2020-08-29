# 단순탐색 (Simple Search)
#   앞에서부터 원하는게 나올 때까지 하나하나 찾는다.

# 장점
#   만들기 쉽다
#   정렬이 안 되어있어도 된다.

# 단점
#   느리다.
#   10억개면 10억개.
#   O(n)

## 대안
#   이진 탐색(Binary Search)
#   O(log N) -> 10억 개면 2x번 정도..

## 단순탐색.
arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]

# 8은 몇 번째에 있을까? -> 7번째. 인덱스로는 6번째
# 입력받은 숫자가 몇 번째 인덱스에 있는지 찾는 function 만들기

def simpleSearch(arr, num):
    result = -1
    for index in range(0, len(arr)):
        if arr[index] == num :
            result = index
    return result
print(simpleSearch(arr, 8))
print(simpleSearch(arr, 10))
print(simpleSearch(arr, 3))