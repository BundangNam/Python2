class 마리오:
    def 공격(self):
        쿠파.목숨 -= 100

class 루이지:
    def 공격(self):
        쿠파.목숨 -= 80

class 버섯도리:
    def 공격(self):
        쿠파.목숨 -= 50

class 쿠파:
    목숨 = 1000
    

m1 = 마리오()
m2 = 루이지()
m3 = 버섯도리()
m4 = 쿠파()

# 공격한다.
# 쿠파를 마리오가 공격한다. 100만큼 쿠파의 목숨을 줄인다.
m1.공격()
# 쿠파를 루이지가 공격한다. 80만큼 쿠파의 목숨을 줄인다.
m2.공격()
# 버섯도리가 쿠파 공격한다. 50만큼 쿠파의 목숨을 줄인다.
m3.공격()

print(쿠파.목숨)

# static == 클래스 영역, 클래스 정적 변수, 클래스 정적 메서드
# 공유 폴더 (ex: 잔디, 웹하드)
# 객체 : 실생활에 있는 물건, 개념

# 로블록스!
# 메타버스!

# 우유의 정보를 저장하는 클래스
# 파일명: 우유
# 가격,크기,우유종류

# 단! 생성자를 이용해서 각각의 데이터를 저장하고
# 출력하세요.

# 초코우유 대형 3500
# 딸기우유 소형 1500
# 바나나우유 중형 2500

class Milk:
    def __init__(self, price, size, kind):
        self.price = price
        self.size = size
        self.kind = kind

        # 자동으로 init 함수가 info호출한다.
        self.info()
    
    def info(self):
        print(self.kind,' ', end='')
        print(self.price,' ', end='')
        print(self.size)

초코 = Milk(3500, '대형', '초코우유')
바나= Milk(2500, '중형', '바나나우유')
딸기 = Milk(1500, '대형', '딸기우유')

class Hero:

    def __init__(self, name, ult, level=10000):
        self.name =name
        self.ult = ult
        level
        
        self.info()
    
    def info(self):
        print(self.name,'', end='')
        print(self.ult)
        
        
토르 = Hero('토르', '망치', level=10000)


        
