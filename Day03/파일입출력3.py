# 파일입출력3.py

# 읽기!
# 1. 파일을 가지고 온다
# 2. 읽는다.
# 3. 파일닫기

file = open('stulist.txt','r')

# 파일 전체 읽기 read()
# 하나의 문자 형태로 반환된다.
# data = file.read()

# 파일 읽기 read(숫자)
# 숫자만큼 읽어온다. 
#data = file.read(10)

# 파일 읽기 readline()
# 한 줄 씩 읽어온다.
#data = file.readline()

# 파일 읽기
# readlines() 안에 잇는 내용을 리스트형태로 반환해준다.
data = file.readlines()
print('replace 전:', data)

# 데이터를 읽어 왔는데 뒤에 줄바꿈 표시를 제거하는 방법
# for문에서 리스트가 오면 리스트의 방번호(인덱스)와
# value 한번에 뽑을 수 있다.
# enumerate(리스트)
for index, string in enumerate(data):
    print(index,' ',string)
    data[index] = string.replace('\n','')
    
#print('replace 후:', data)
file.close()

class Stu:
    def __init__(self,name,dept,hakbun):
        self.name = name
        self.dept = dept
        self.hakbun = hakbun

print(data)

for value in data:
    str1 = value.split(':')
    print(str1[1])




# 파일입출력시 텍스트 파일로 저장을 하면
# 내 컴퓨터에서만 확인이 가능하다.

# 데이터베이스라는 서버를 이용해서 누구든지 수정하고 삭제,
# 조회할 수 있도록 실시간으로 데이터를 학인할 수 있는
# 관리 프로그램이 필요하다.
# DBMS라고 한다.
# sql 언어 -> 데이터베이스를 조작하는 언어

# sqllite3 
# 파이썬에서 기본적으로 데이터베이스를 제공한다.

import sqlite3

# 
