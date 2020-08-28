import math

# 좌표평면의 두 점 사이 거리 구하는 알고리즘
# 좌표평면 = x축, y축
# (x,y)
# (1,0) 1행 0열
# (1,2) 1행 2열
# (3,0) 3행 0열
# 두 점 사이의 거리 = root((x1-x2)^2 + (y1-y2)^2))

def distance(dot1, dot2):
    xDistance = dot1[0] - dot2[0]
    yDistance = dot1[1] - dot2[1]
    # import math
    # math.pow
    # math.sqrt

    return math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))

a = (1, 2)  # 튜플
b = (10, 15)
print(distance(a,b))