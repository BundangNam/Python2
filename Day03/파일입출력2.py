#파일입출력2.py


# 파일이름 : stulist.txt

file = open('stulist.txt','w')

# 학생의 정보를 5명 입력해주세요!
#  이서희 1001 법학과
#  이지희 1002 체육과
#  이정희 1003 컴퓨터공학과
#  강동원 1004 천사과
#  이준기 1005 디자인과 

# start = 1

# while start <= 5:

#     name = input('이름:')
#     hakbun = int(input('학번:'))
#     dept = input('학과:')

#     file.write('이름:' + name + '\n')
#     file.write('학번:' + str(hakbun) + "\n")
#     file.write('학과:' + dept + '\n')

#     start = start +1


# file.close()

# 서희가 건강검진 센터에서 일을 한다.
# 각각의 텍스트 파일을 생성 
list1 = ['뽀로로','크롱','루피','패티','에디','포비']

for value in list1:
    file = open(value +'.txt','w')
    file.write()



# 뽀로로 건강검진.txt
#  이름: 뽀로로
#  성별: 남자
#  핸드폰: 010-1111-1111
#  키 : 100 cm
#  몸무게 : 30 kg
#  혈액형: A형
#  
# 크롱 건강검진.txt
#  이름: 크롱
#  성별: 남자
#  핸드폰: 010-1111-2222
#  키 : 80 cm
#  몸무게 : 20 kg
#  혈액형: B형 

# 루피 건강검진.txt







'''
#파일입출력2.py


# 파일이름 : stulist.txt

file = open('stulist.txt','w')

# 학생의 정보를 5명 입력해주세요!
#  이서희 1001 법학과
#  이지희 1002 체육과
#  이정희 1003 컴퓨터공학과
#  강동원 1004 천사과
#  이준기 1005 디자인과 

start = 1

while start <= 5:
    file.write('이름:' + name + '\n')
    #file.write(f'학번:{hakbun}\n')

# 숫자 -> 문자로 변경 
file.write('학번:' + str(hakbun) + "\n")
file.write('학과:' + dept + '\n')

file.close()




'''

    
