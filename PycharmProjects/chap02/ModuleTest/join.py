# join.py
def existId(id):
    print("ID 중복 검사를 수행합니다. ")
    return 0

def makeId(id, pw, name, phone) :
    check = existId(id)
    if check == 0 :
        print("사용가능한 ID입니다. ")
        info = {"ID":id, 'PW':pw, "Name":name, "Phone":phone}
        return info
    else:
        print("이미 존재하는 ID입니다. 다른 아이디를 입력해주세요. ")
