# 재귀(recursive)
#   자기 자신을 호출 하는 것.

# 재귀함수 (recursive function)
#   자기 자신을 호출하는 함수.

    ## 예시
    # def sum(arr):
    #     return sum(arr)
    # print(sum(5))

# 재귀함수 만들기
#   탈출 조건, 끝나는 조건이 꼭 들어가야 한다.


# arr의 모든 값을 더하는 함수를 만들어보자.
arr = [7, 3, 2, 9]

def sum(arr, accu):
    #   pop()   :   array의 맨 뒤의 값을 추출
    if (len(arr) == 0) : return accu
    return sum(arr, accu + arr.pop())  # 여기에서 멈추면 pop() 할 것이 없기 때문에 error가 발생할 것

result = sum(arr, 0)   # 21. 초기값은 0으로 넣어준다
print("result:",result)
