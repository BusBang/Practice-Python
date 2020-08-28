import re   # regular expression 모듈

# pat = re.compile("찾으려는 문자열")    #\d\d\d-\d\d\d\d-\d\d\d\d
# mch = pat.search("조사할 문자열")
# if mch :
#     print("Found !")
# else :
#     print("Not Found !")
# 입력 형식 검사

# 대소문자를 구분한다.
# 공백, 엔터, tab 등 모두 패턴의 일부이다.

#첫 매칭 문자열 찾기 : search(), match()
pat = re.compile("CAT")
m = pat.search("WHITECATBROWNCAT")
print(re.compile("WHITE").search("WHITECATBROWNCAT").group())
print(m.group())

noRex = re.compile("\d\d\d-\d\d\d-\d\d\d\d")
p = noRex.search("My Office Number Is Not 010-5555-5555, This Is 010-555-5555")
print("office number is : ",p.group())

#모든 매칠 문자열 찾기 : finall()
m = pat.findall("WHITECATBROWNCAT")
print(m)

#-----------------

# 메타문자
# : 반복 메타문자, 매칭 메타문자
# 반복 메타문자
#   - 특정 패턴의 반복을 표현
#   패턴* : 패턴이 0회 이상 반복되면 매치
#   패턴+ : 패턴이 1회 이상 반복되면 매치
#   패턴? : 패턴이 0회이거나 1회 반복되면 매치
#   패턴{m} : 패턴이 m회 반복되면 매치
#   패턴{m,n} : 패턴이 m회부터 n회까지 반복되면 매치
#   패턴{m,} : 패턴이 m회 이상 반복되면 매치
