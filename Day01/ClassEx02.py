# 영화를 예매하는 클래스
# 영화 제목
# 영화 상영 시간(영화를 보는 시간)
# 영화 시작시간
# 상영관
# 예매번호
# 인원수

# 클래스를 작성할 때는 무조건 첫글자는 대문자
class Movie:
    
    title = ''
    time = ''
    s_time = ''
    where = ''
    num = ''
    

# 함수 ! (반복되는 명령문들을 하나로 묶음.)
def init(who, title, time, s_time, where, num):
    who.where = where
    who.title = title
    who.time = time
    who.s_time = s_time
    who.num = num

# 실제 변수 생성(객체)
yang = Movie()
init(yang, '범죄도시3', 105, 24, '3관', 2)


zee = Movie()
init(zee, '가디언즈오브갤럭시3', 150, 22, '4관', 2)
# zee.title = '가디언즈오브갤럭시3'
# zee.time = 150
# zee.s_time = 22
# zee.where = '4관'
# zee.num = 2

goo = Movie()
init(goo, '아이언맨', 100, 23, '1관', 2)

class ATM:
    
    색상 = ''
    크기 = ''
    은행명 = ''

# atm기계 가장 큰 역할: 출금
    def 출금(카드):
        #비밀번호 확인 -> 잔액까지 조회
        출금액 = int(input('출금액> '))
        # 카드 잔액에 따라서 잔액이 출금액보다 크면 출금이 가능하다.
        # 출금액이 카드잔액보다 크다 -> '한도 초과'

        if 출금액 <= 카드:
            print('출금가능!')
        else:
            print('한도 초과ㅜ')

혜나 = ATM()
혜나.출금()

미선 = ATM()
미선.출금()

혜나 = 출금()
미선 = 출금()
유림 = 출금()
미나 = 출금()

서희 = 출금()
    



