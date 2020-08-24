weight = 10
day = 0
while weight > 0 :
    day += 1
    print(day, "일째")
    if day == 3 :
        print("다이어트 포기 !! ㅠㅠ")
        #break   # 여기서 while문을 빠져나온다.
        continue    #여기서 다이어트를 한 번 쉰다. 그래서 11일까지 가게 된다. 아래 문장들을 실행하지 않는 것.
    print("운동 열심히 !!")
    weight -= 1

print("살은 빼서 뭐해 ㅡ,.ㅡ")