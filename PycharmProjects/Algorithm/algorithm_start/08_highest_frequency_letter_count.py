# 가장 많이 등장하는 알파벳의 갯수 구하기
# ex) mouse : 1, test :2, hello : 2

word = "test"

def highFrequencyLetterCount(word) :
    # print(word[0])  # String의 첫 번째 글자가 나온다.
    map = {}
    for alpha in word:
        if map.get(alpha) == None:
            map[alpha] = 1
        else:
            map[alpha] += 1
    max = -1
    # letter = ''
    for key in map:
        if map[key] > max :
            max = map[key]
            # letter = key
    return max
print("result = ",highFrequencyLetterCount(word))
print("result = ",highFrequencyLetterCount("welcome to blackparade"))