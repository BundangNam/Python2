# 수강신청관리프로그램.py

# 한명의 학생이 수강신청을 할 때는 
# 수강신청  (subject)
# 과목명
# 과목시간
# 과목점수

# 학생 Student
#  이름
#  학과
#  학번
#  수강신청을 하는 과목을 저장하는 리스트!


# 학교에서 학생들을 관리하는 리스트!

class Student:

    def __init__(self,name,dept,hakbun):
        self.name = name            # 이름
        self.dept = dept            # 학과
        self.hakbun = hakbun        # 학번
        self.sub = []               # 수강신청리스트
        self.login = False          # 로그인 변수
        # true 이면 로그인 중!
        # false 이면 로그 아웃!

        self.stu_info()            # 학생의 정보를 출력하는 함수를 호출한다

        # 회원가입을 할 때 수강신청까지 막 바로 하지 않고
        # 회원가입하고 나서 수강신청을 추가할 것이다!

    def stu_info(self):

        print()
        print()

        print("이름: " ,self.name)
        print("학과: " ,self.dept)
        print("학번: " ,self.hakbun)

        # 리스트의 결과 값이 비어있으면 false 
        # 리스트의 값이 하나라도 있으면 true
        # 그거에 따라서 출력을 해야되는 상황이 달라진다.
        res = bool(self.sub)

        if res:  
            for i in self.sub:
                print(i)

        else:
            print(" 아직 수강 신청을 하지 않았습니다!")
        
        print()  # 공백 두개 줌
        print()



school = []

# bool()
# 참과 거짓으로 결과가 나온다.
# 리스트의 값이 비었는지 안 비었는지
# 확인하기 위해서 사용한다. 

print(bool([]))
print(bool([10]))




while True:

    print(" 수강신청,회원 가입, 로그인 , 종료 ")
    select = input('원하는 메뉴를 입력: ')

    if select == "수강신청":
        # 로그인이 되어있는 상태만 수강신청 가능하다!
         if ??? == True:
            print('로그인 중~~~`')
        else:
            print('로그인하세요!!!')
        pass

    elif select == '회원가입':

        # 회원가입하는 내용을 입력 받는다 
        name = input('이름> ')
        hakbun = int(input('학번> ')) 
        dept = input('학과> ')

        # 학생의 클래스를 만든다 학생의 새로운 변수를 생성한다. 
        temp = Student(name,dept,hakbun)

        # 학생을 관리하는 school 리스트에 학생을 추가한다.
        school.append(temp)

        # 생성자에 들어가는 (변수들) 왼쪽부터 순서대로 매칭 시킨다.
        # 원래 student 매개변수순서는 name,dept,hakbun 정상적인 변수 생성
        #  Student(dept = dept, hakbun = hakbun, name = name)
        # 매개변수가 순서 상관없이 ㅋ늘래스 안에 변수에 저장 될 수 있도록 매칭시켜줌.
        # 파이썬만의 기능

        #로그인을 즉 회원가입이 되면 로그인중으로 
        # self.login 값을 true로 변경 할 것!
        print(" 회원가입을 축하합니다!")

        

    elif select == "로그인":
        # 로그인 이름,학번을 받는다. 
        now_hakbun = int(input('학번> ')) 
        

        # 검색
        for student in school:
            print(student.hakbun)

    elif select == "종료":
        print(" 프로그램을 종료합니다! bye~")
        break

    else:
        print(" 제대로 입력해주세요~ 콱~~~!!!")

# 이 프로그램에 제일 큰 문제가 바로 저장이 안됨
# 프로그램 실행 중에는 데이터가 살아있다.
# 프로그램이 종료되면 기존에 데이터가 싹 다 사라진다.

# 프로그램이 시작이 되면 기존에 데이터를 불러오는 파일입출력!


# 과제
# 1. 3명의 데이터를 저장하세요.
#   이서희 1001 프로그래밍ㅅ
#   이지희 1002 프로그래밍
#   이정희 1003 프로그래밍

#  수강신청 들어가서 
#  학번을 입력해서 이서희의 학번이면
#  이서희한테 수강신청 객체를 생성하면 된다.

#  파이썬 오전10시 미정
#  자바   오후01시 미정
#  html   오후12시 미정
#  spring 오후03시 미정

# 수강신청 클래스 정의 하고 수강신청 로그인이 되어있다면
# 수강신청 객체 생성 후 로그인 된 학생의 리시트에 저장하기.
# 수강신청에 대한 출력