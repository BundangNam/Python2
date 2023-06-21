# 파일명: 그래픽1.py

import tkinter as t
#from tkinter.messagebox import messagebox   # 팝업창을 사용하려면 포함해야되는
                                         # 라이브러리!
import tkinter.messagebox as messagebox

def click():
    # 클릭했을 때 entry 입력창의 값을 가져온다.
    # get()
    # 내용을 팝업창에 출력한다.
    data = entry1.get()  #set()
    messagebox.showinfo("타이블",data)


def myFunc():
    if chk.get() == 0:
        messagebox.showinfo("","체크버튼 off 네요..")

    else:
        messagebox.showinfo("","체크버튼 on 이네요..")
        
    
    
window = t.Tk() 
window.geometry("640x400+100+100")

# 라벨
# 문자를 표현할 수있다.

label1 = t.Label(window,text="아이디")
label1.pack()


#input == Entry()
entry1 = t.Entry(window)
entry1.pack()


# 버튼
btn = t.Button(window,text="가입하기",command=click)
btn.pack()

# 체크박스

chk = t.IntVar()   # 체크박스가 체크된 값과 체크되지 않은 값을 저장하는 변수
cb1 = t.Checkbutton(window,text="클릭하세요",variable=chk,command=myFunc)
cb1.pack()


window.mainloop()    









'''
# 실제 창크기, 위치 조절 등을 설정
window.title("내가 만든 윈도우!")
# geometry("너비x높이+x좌표+y좌표")
window.geometry("640x400+100+100")

# 자동 창 크기 조절 기본 설정값이 True -> False 로변경하면 자동
# 크기 조절을 할 수 없다.
window.resizable(False,False)

#bg ="원하는 배경색"
#fg ="원하는 문자열의 색상"
# command=show
#  버튼이 클릭시 동작하는 함수명 작성한다. 실행을 한다.

# 이미지를 먼저 파이썬 안으로 가지고 와야된다.
img = t.PhotoImage(file ="Z:\\이서희\\파이썬2\\Day4\\ryan.png")


#버튼 
mybtn1 = t.Button(window,text="버튼1",bg="pink",command=show)
mybtn1.pack()         # 윈도우창에 버튼을 붙이는 함수

mybtn2 = t.Button(window,text="버튼2",bg="blue",fg="white",command=btn2)
mybtn2.pack() 

# 3번째 버튼에 라이언이미지버튼을 만드시오!
mybtn3 = t.Button(window,image=img)
mybtn3.pack()

# 함수 작성(버튼을 눌렀을 떄 기능)
def show():
    print("왜 눌렀니??")


def btn2():
    #버튼2번을 눌렀을 때 hello python! 글자가 출력되게 하시오!
    print("hello python!")


# 파이썬에서 그래픽을 이용해서 프로그램을 만들 수 있게 
# 도와주는 라이브러리는 tkinter 클래스 

# 버튼,스크롤,마우스포인터,슬라이드, 메뉴 등등
# 컴포넌트 (택배상자 )

# 한군데 모아서 프로그램을 만들어야된다 그때 모아지는 판
# 윈도우 판

# 라이브러리의 이름이 길면 작성하다가 오타가 나는 경우가 많다
# as 새이름

'''