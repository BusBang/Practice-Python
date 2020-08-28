# 퀵 정렬

# 정렬의 종류 : 버블, 선택, 삽입, 병합, 퀵
# 퀵 정렬 : n * log N

numbers = [40, 35, 27, 50 ,75]
def quickSort(array):
    # 재귀함수, 탈출조건을 만들어야 함
    if len(array) < 2:
        # array의 길이가 2보다 작을 때 탈출
        return array
    else:
        pivot = array[0]    # numbers[0]을 기준으로 잡는다 1회 : 40. 2회 35.

        # 파이썬 축약 문법. array[1:]의 number 들 중, pivot 보다 작거나 같은 것을 뽑아라
        less = [number for number in array[1:] if number <= pivot]
        print("less:",less)     # 1회때, [35, 27]이 나와야 함

        # 파이썬 축약 문법. array[1:]의 number 들 중, pivot 보다 큰 것을 뽑아라
        greater = [number for number in array[1:] if number > pivot]
        print("greater:",greater)     # 1회때, [35, 27]이 나와야 함

        # pivot은 int이기 때문에 list로 만들어줘야한다
        # less와 greater에 재귀함수를 적용한다.
        return quickSort(less) + [pivot] + quickSort(greater)

result = (quickSort(numbers))
print(result)

result = (quickSort([10, 20, 5, 2, 3, 1, 0, 100, 200]))
print(result)

