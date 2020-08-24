import matplotlib.pyplot as plt

empty = []
number = [1,2,3]
test = [1,2,3,'안녕','하세요']
print(empty)
print(number)
empty = [1,2]
print(empty)
print("empty : "+str(empty[0]))
# print("empty : "+str(empty[2]))   --> list index out of range
print(test[4])
print(test[-1])
print(test[0:4])
# test2 = input("ㅎㅎㅎ")
# print(test2)
print(number[0:3])
number[2] += 3
print(number[2])
meal=[[1,2,3],[4,5,6],[7,8,9]]
print(meal)
print(meal[0])
print(meal[0][2])

# 그래프 그리기
# x=[1,2,3]
# plt.bar(x,number)
# plt.show()

######################

#list 실습
meal_cal = [[500, 1300, 700],[700, 1300, 700], [900, 1300, 400]]
print(meal_cal[2][1])
cal2 = [1950, 2350, 1850, 2200, 3800, 2800, 2000]
x = [1,2,3,4,5,6,7]
plt.bar(x,cal2)
plt.show()