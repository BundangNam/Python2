import tkinter as t

def myFunc():
    if myVar.get() == 1:
       label1.configure(text="사과")

    elif myVar.get() == 2:
        label1.configure(text="바나나")
    
    elif myVar.get() == 3:
        label1.configure(text="딸기")
    
    else:
        label1.configure(text="귤")



win = t.Tk()
win.geometry("300x200")

label1 = t.Label(win,text="과일 1개 선택")
label1.pack()
myVar = t.IntVar()

rb1 = t.Radiobutton(win,text = "사과",variable=myVar, value = 1, command= myFunc)
rb1.pack()

rb2 = t.Radiobutton(win,text = "바나나",variable=myVar, value = 2, command= myFunc)
rb2.pack()


rb3 = t.Radiobutton(win,text = "딸기",variable=myVar, value = 3, command= myFunc)
rb3.pack()

rb4 = t.Radiobutton(win,text = "귤",variable=myVar, value = 4, command= myFunc)
rb4.pack()

btn = t.Button(win,text="과일 선택")
btn.pack()


win.mainloop()
