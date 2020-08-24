
#예제 1) 커피자판기
# -호출할 때, 2가지 인수를 넣어준다. (돈, 커피 종류)
# -화면에 주문한 음료가 나왔음을 출력해준다. (xx가 나왔습니다)
# -잔돈을 반환값으로 내보낸다.

def printName(str) :
    print(str+'가 나왔습니다')

def coffeeMachine(money, name):
    if name == '아메리카노':
        price = 1100
        printName(name)
    elif name == '에스프레소':
        price = 1000
        printName(name)
    elif name == '밀크티':
        price = 900
        printName(name)
    else :
        price = 0
        print(name,'은 없습니다.')
    change = money - price
    return change

print(coffeeMachine(2000, '아메리카노'))
print(coffeeMachine(3000, '밀크티'))
print(coffeeMachine(4400, '에스프레소'))