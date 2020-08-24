#1)
money = 1000
water = 500
if water < money :
    print("생수를 뽑는다")
    print("물을 마신다")
print()
#2)
a = 3
b = 5
print(a < b)    #True
print(a >= b)   #False
print(a != b)   #True
print("Korean" in ["Korean", "English"])    #True
print()
#3)
if "커피" not in ["우유", "녹차", "홍차"]:
    print("우유 주세요")

if "커피" not in ["커피", "우유", "녹차", "홍차"]:
    print("우유 주세요")
else :
    print("커피 주세요")