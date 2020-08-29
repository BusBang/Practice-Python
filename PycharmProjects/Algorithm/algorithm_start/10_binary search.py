# 이진탐색 (binary search)
#   탐색 범위를 절반씩 줄여나가면서 찾는다
#   O(log n)

## 장점
#   빠르다
#   실제로 쓰인다

## 단점
#   정렬이 되어있어야 한다.
#   만들기 어렵다 (단순 탐색과 달리 중간값을 찾고, 시작과 끝점을 만들어줘야 한다. )

## 핵심 로직
# 중간 인덱스 값을 구한다. (10억개 -> 5억개, 5억개 -> 2.5억)
# 0--------------5----------9.6--10
# 5-------------------------9.6--10
# 7.5----------------------9.6---10

arr = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
#   10 -> 8
def binarySearch(arr, target) :
    start = 0
    end = len(arr) - 1
    while start <= end :
        # midIndex = len(arr) // 2    # // : 나머지를 버린 몫
        midIndex = (start + end) // 2

        if arr[midIndex] == target :
            return midIndex
        elif arr[midIndex] < target:
            # 중간값이 목표값보다 작은 경우
            start = midIndex + 1
        elif arr[midIndex] > target:
            # 중간값이 목표값보다 큰 경우
            end = midIndex - 1
    return -1

print(binarySearch(arr, 8))
print(binarySearch(arr, 3))
print(binarySearch(arr, 5))
print(binarySearch(arr, 4))
# print(arr[2:])