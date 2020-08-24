# dictionary는 키와 값을 갖는다 -> list와 달리 중괄호를 씀

fruit = {'사과':'apple', '바나나':'banana', '파인애플':'pineapple'}
print(fruit)

# 1. 중복된 키를 가질 수 없음. 덮어써짐
# 2. value엔 문자, 숫자, 리스트가 올 수 있다.

print(fruit.keys())
print(fruit['사과'])  #검색을 할 땐 대괄호를 쓴다!

fruit['토마토'] = 'tomato' # 추가할 땐 변수명[키값]=값
print(fruit)

del fruit['토마토']
print(fruit)    # 키를 삭제 !

#Dictionary 예제

food = {'닭갈비':'춘천', '한우':'횡성', '밀면':'부산', '비빔밥':'전주'}
print(food['비빔밥'])
food['부대찌개'] = '의정부'
del food['한우']
print(food)