# 파일 테스트

f = open("C:\\python_test\\food.txt", 'w')
f.write("떡볶이\n")
f.write("피자\n")
f.close()

f = open("C:\\python_test\\food.txt", 'r')
data = f.read()
print(data)
f.close()

f = open("C:\\python_test\\food.txt", 'r')
list = f.readlines()
print(list)
print(list[0])
print(list[1])
f.close()

f = open("C:\\python_test\\food.txt", 'a')
f.write('파스타')
f.close()

f = open("C:\\python_test\\food.txt", 'r')
list = f.readlines()
print(list)
f.close()