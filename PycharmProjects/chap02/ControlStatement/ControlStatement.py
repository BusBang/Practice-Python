#if문
# if 조건 :
#   실행할 문장1
#   실행할 문장2
# else 조건 :
#   실행할 문장1
#   실행할 문장2

#   비교연산 :  ==, !=, <=, >=, <, >
#   논리 기호 : x and y, x or y, not x
#   값의 존재 여부 : in, not in

#if 예제
money = 1000
water = 500
if water < money :
    print("생수를 뽑는다")
    print("물을 마신다")
        # print("시원하다")   <- 들여쓰기 오류.
print("---------------------")

#while문
#while 조건 :
#   문장1
#   문장2

weight = 10
day = 0
while weight>0:
    day += 1
    print(day, "일째")
    print("07시 기상, 아침 식사, 운동")
    print("점심 식사, 운동")
    print("저녁 식사, 운동, 취침")
    weight -= 1
#하루 운동시마다 1kg씩 감량한다는 가정

print("--------------")

#for문
# for 변수 in 집합 자료(리스트):
#     문장1
#     문장2

#예제1)
dict = ["Korean", "English", "French"]
for lang in dict :
    print(lang)

#예제2)
myScores = [60, 75, 80, 75]
total = 0
for score in myScores :
    total += score
    print(total)
print("총합 : ", total)

#   range() 함수
#       range(끝)                  :  range(5)         =>  0, 1, 2, 3, 4
#       range(시작, 끝)            :  range(1, 5)      =>  1, 2, 3, 4
#       range(시작, 끝, 증가 단위) :  range(0, 10, 2)  =>  0, 2, 4, 6, 8
#range() 예시.
sum = 0
for num in range(1, 11):
    sum += num
print("sum:",sum)

#break와 continue
#break : 반복문을 강제로 빠져나옴
#continue : 현재 진행중인 작업을 중단하고 while이나 for의 조건 부분으로 돌아가 다시 조건 확인