dictionary = ["Korean", "English", "French"]
for language in dictionary :
    print(language)

print("------------")
myScores = [60, 75, 80, 75]
total = 0
for score  in myScores :
    total += score
    print(total)
print("총합",total)

print("--------")
for num in range(5) :
    print("num:",num)

print("--------")
for num in range(1,5) :
    print("num:",num)

print("--------")
for num in range(0, 11, 2) :
    print("num:",num)
print("------------")
list = [1,2,3,4,5,1,2,3,4,5]
print(list)
for number in range(list[2], list[4]) :
    print(list[2],"부터",list[4],"까지")
    print("number:",number)