# mysql2.py

# 데이터베이스를 만드는 순서
# 첫번째
# 데이터베이스를 만든다.

from sqlite3 import *
'''
# 1. 데이터베이스 연결(연동) 생성
con = connect("C:\\AAA\\memberlist.db")

# 2. 테이블생성
cur = con.cursor()

sql = "create table member(id text,pw text , name text , hakbun integer)"

#전송
cur.execute(sql)

# 닫기 
con.close()
'''
con = connect("memberlist.db")
cur = con.cursor()

# 추가하는 내용을 적는다
# sql = 'insert into member values("love","love","이서희",1001)'
# sql = 'insert into member(id,pw,name,hakbun) values("qwer","qwer","이지희",1002)'

# 그때그떄마다 원하는 값으로 데이터를 저장하고 싶으면
dbid = input('아이디:')
dbpw = input('비번:')
name = input('이름:')
hakbun = int(input('학번:'))

#cur.execute('insert into member(id,pw,name,hakbun) values(?,?,?,?)',(dbid,dbpw,name,hakbun))

#cur.execute(sql)


data = [
    ("love","love","이서희",1001),
    ("qwer","qwer","이지희",1002),
    ("poiu","poiu","이정희",1003)
]
cur.executemany('insert into member values(?,?,?,?)',data)
con.commit()
con.close()