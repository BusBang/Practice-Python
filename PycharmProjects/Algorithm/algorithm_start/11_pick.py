# pick
#   배열에서 2개, 3개, n개 고르기

## 2개 고르기 -> nC2
# arr = [1, 2, 3, 4, 5, 6, 7]
# (1, 2), (1, 3), (1, 4) --- (1, 7)   -6개
# (2, 3), (2, 4), (2, 5) --- (2, 7)   -5개

## 규칙
# 1포함 6개
# 2포함 5개
# 3포함 4개

arr = [1, 2, 3, 4, 5, 6, 7]

def pick2(arr):
    list = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            list.append((arr[i], arr[j]))
    return list

## 3개 고르기 -> nC3
# arr = [1, 2, 3, 4, 5]
# (1, 2, 3), (1, 2, 4), (1, 2, 5) - 3개
# (1, 3, 4), (1, 3, 5) - 2개
# (1, 4, 5) - 1개
# (2, 3, 4), (2, 3, 5) - 2개
# (2, 4, 5) - 1개
# (3, 4, 5) - 1개

def pick3(arr):
    list = []
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                list.append((arr[i], arr[j], arr[k]))
    return list

print(pick2(arr))
print(len(pick2(arr)))
print(pick2([1,2,3,4,5,6,7,8,9,10,11,12]))
arr2 = [1,2,3,4]
print(pick3(arr2))
print(len(pick3(arr2)))
