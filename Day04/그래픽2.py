# 그래픽2.py

# import 라이브러리명을 쓴다.
#     라이브러리가 어디 있는지 위치만 가져온다. 경로만 검색한다.

# from 라이브러리 import *
#  라이브러리의 안에 있는 모든 내용을 복사해서 현재 파일로 붙여넣기한다.
from tkinter import *

# 라디오버튼
# 여러개 중에 하나의 결과를 얻을 떄 사용하는 버튼

def myFunc():
    if myVar.get() == 1:
       label1.configure(text="벤츠")

    elif myVar.get() == 2:
        label1.configure(text="BMW")

    else:
        label1.configure(text="아우디")


win = Tk()

win.geometry("300x200")
myVar = IntVar()

rb1 = Radiobutton(win,text = "벤츠",variable=myVar, value = 1, command= myFunc)
rb1.pack()

rb2 = Radiobutton(win,text = "BMW",variable=myVar, value = 2, command= myFunc)
rb2.pack()


rb3 = Radiobutton(win,text = "아우디",variable=myVar, value = 3, command= myFunc)
rb3.pack()

label1 = Label(win,text="선택한 차량:",fg = "red")
label1.pack()








win.mainloop()