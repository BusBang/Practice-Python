# 컴퓨터 파일

# 파일 경로 : 파일이 실제 위치한 디렉터리 명을 계층 구조로 나열
# 파일 사용의 유용성 :
#   - 장기간 보관하거나 이후 재사용 및 공유 가능
# 파일로 저장한 후, 파이썬을 통해 데이터를 읽어들여 데이터를 분석하고 그 결과를 역시 파일로 저장

# 파일 열기
# 파일변수 = open(파일 경로, 모드)
# 파일 모드 :
#   r : 파일을 읽기만 할 때 사용 (해당 경로에 파일이 없으면 에러)
#   w : 파일에 내용을 쓸 때 사용 (덮어쓰는 것. 기존 내용이 모두 삭제 됨. 파일이 없으면 생성)
#   a : 파일 마지막에 내용을 추가할 때 사용 (현재 파일 내용 뒤에 기록. 파일이 없으면 생성)

# f = open("C:\\python\\newfile.txt", 'r')
# f = open("newfile.txt", 'w')
# f = open("C:\\python\\newfile.txt", 'a')

# 파일 쓰기
# 파일변수.write(기록할 문자열)
# f= open("C:\\python\\food.text", 'w') #파일 열기
# f.write("떡볶이\n")
# f.write("피자\n")

# 파일 읽기
# 파일 내용을 읽어오는 함수
# 변수 = 파일변수.read()      : 파일의 내용 전체를 한꺼번에 읽음
# 변수 = 파일변수.readline()  : 호출할 때 마다 파일의 내용을 줄 단위로 읽음
# 변수 = 파일변수.readlines() : 파일 모든 내용을 읽어 줄 단위로 리스트 항목을 만들어줌

# f = open("C:\\python\\text.text", 'r')
# data = f.read()
# print(data)

# f = open("C:\\python\\text.text", 'r')
# line1 = f.readline()

# f = open("C:\\python\\text.text", 'r')
# line1 = f.readline()
# print(line1)
# 떡볶이
# line2 = f.readline()
# print(line2)
# 피자

# f = open("C:\\python\\text.text", 'r')
# data = f.readlines()
# print(data)
# ['떡볶이\n', '피자\n']

# 파일 닫기
# 변수명.close()