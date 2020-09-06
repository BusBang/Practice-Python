#백준 1712 손익분기점 문제

#A : 고정비, B : 가변비, C : 노트북 가격
A, B, C = list(map(int,input.split(' ')))
BEP = 0
if C <= B :
    BEP = -1
else :
    BEP = A // (C-B) -1
print(BEP)