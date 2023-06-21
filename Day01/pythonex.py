# 실행 ctrl + f5
print()     # 줄바꿈
print('home!!')

# 클래스 복습문제

# 기차를 예매하는 프로그램을 만든다!
# 회원의 정보를 저장할 클래스를 작성

# 클래스명: train-rev
# 아이디, 패스워드, 이름, 폰번호, 예약 =[]
class train_rev:
    
    id = ''
    pw = ''
    name = ''
    num = ''
    rev = []

# 무한 반복을 이용해서 종료 입력하면 프로그램을 종료!
# 1. 회원가입

# 문자 안에서 특정한 행동을 하는 특수문자
# ' \t      '  탭만큼 이동

# 여러개의 회원을 저장하는 리스트
train_list = []
while True:
    print('--------------srt 열차 예매 입니다.--------------')
    print('\t1. 회원가입')
    print('\t2. 회원조회')
    print('\t3. 로그인')
    print('\t4. 로그아웃')
    print("\t   '종료' 입력하면 프로그램 종료된다.")
    print('-'*45)

    select = input('>')

    if select == '종료':
        break
    
    if select == '1':
        db_id = input('아이디> ')
        db_pw = input('패스워드> ')
        db_name = input('이름> ')
        db_num = input('폰번호> ')
        
        

        # 내가 입력하는 데이터들이 모두 같은 타입이면 사용이 가능하다.
        # map(변경할 타입, input().split('구분자'))
        # input().split('구분자') -> 리스트형태로 반환된다.
        # map() 함수 -> 파이선이 미리 만들어 놓은 함수.
        #   객체형태로 돌려준다. 객체를 접근하는 방법으로 써야된다.
        
        """list1 = list(map(str, input('>').split(',')))
        print(list1)
        
        str_list = input().split('')
        print(str_list)"""

        temp = train_rev()  # 내가 만든 변수를 생성했다.

        temp.id = db_id
        temp.pw = db_pw
        temp.name = db_name
        temp.num = db_num
        
        #정상적으로 저장이 된다면 첫번째 이서희, 이지희라는 사람의 내용이 각각 저장됨.
        print(temp.id)
        
        
        # 입력받은 데이터를 temp 변수에 저장 후 출력

    elif select == '2':
        print(temp)     # 실제 내용이 저장되어있는 temp 라는 변수 출력
        
    elif select == '3':
        pass
    elif select == '4':
        pass
    else: # 예외적인 메시지를 작성해야된다.1
        print('1~4까지만 입력하세요!')