from tkinter import *
import random

set_text = "Hello"

prizes = [1,5,10,25,50,100,250,500,1000,1250,5000,10000,25000,50000,100000]
showprizes = prizes.copy()
random.shuffle(prizes)
selectingbox = True

win = Tk()

def boxclick(x,t,selbox,box):
    if selbox == True:
        global playerbox
        playerbox = x

        global selectingbox
        selectingbox = False

        if x==1:
            global box1
            box1.destroy()
            box1 = Button(win, bg = "medium orchid", text="YOUR BOX\nBox 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
            box1.grid(row=1,column=0)
        if x==2:
            global box2
            box2.destroy()
            box2 = Button(win, bg = "medium orchid", text="YOUR BOX\nBox 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
            box2.grid(row=1,column=0)
        if x==3:
            global box3
            box3.destroy()
            box3 = Button(win, bg = "medium orchid", text="YOUR BOX\nBox 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
            box3.grid(row=1,column=0)
        if x==4:
            global box4
            box4.destroy()
            box4 = Button(win, bg = "medium orchid", text="YOUR BOX\nBox 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
            box4.grid(row=1,column=0)
        if x==5:
            global box5
            box5.destroy()
            box5 = Button(win, bg = "medium orchid", text="YOUR BOX\nBox 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
            box5.grid(row=1,column=0)
        #CONTINUE HERE

    t.destroy()
    if x==1:
        t=Label(win, text="Opening Box 1")
    elif x==2:
        t=Label(win, text="Opening Box 2")
    elif x==3:
        t=Label(win, text="Opening Box 3")
    elif x==4:
        t=Label(win, text="Opening Box 4")
    elif x==5:
        t=Label(win, text="Opening Box 5")
    elif x==6:
        t=Label(win, text="Opening Box 6")
    elif x==7:
        t=Label(win, text="Opening Box 7")
    elif x==8:
        t=Label(win, text="Opening Box 8")
    elif x==9:
        t=Label(win, text="Opening Box 9")
    elif x==10:
        t=Label(win, text="Opening Box 10")
    elif x==11:
        t=Label(win, text="Opening Box 11")
    elif x==12:
        t=Label(win, text="Opening Box 12")
    elif x==12:
        t=Label(win, text="Opening Box 13")
    elif x==12:
        t=Label(win, text="Opening Box 14")
    elif x==12:
        t=Label(win, text="Opening Box 15")
    t.grid(row=0,column=0)

    global label
    label = t

label = Label(win, text = "Hi hello there!")
label.grid(row=0,column=0)

box1= Button(win, text="Box 1",height=3,width=14,command=lambda: boxclick(1,label,selectingbox,box1))
box2= Button(win, text="Box 2",height=3,width=14,command=lambda: boxclick(2,label,selectingbox,box2))
box3= Button(win, text="Box 3",height=3,width=14,command=lambda: boxclick(3,label,selectingbox,box3))
box4= Button(win, text="Box 4",height=3,width=14,command=lambda: boxclick(4,label,selectingbox,box4))
box5= Button(win, text="Box 5",height=3,width=14,command=lambda: boxclick(5,label,selectingbox,box5))
box6= Button(win, text="Box 6",height=3,width=14,command=lambda: boxclick(6,label,selectingbox,box6))
box7= Button(win, text="Box 7",height=3,width=14,command=lambda: boxclick(7,label,selectingbox,box7))
box8= Button(win, text="Box 8",height=3,width=14,command=lambda: boxclick(8,label,selectingbox,box8))
box9= Button(win, text="Box 9",height=3,width=14,command=lambda: boxclick(9,label,selectingbox,box9))
box10= Button(win, text="Box 10",height=3,width=14,command=lambda: boxclick(10,label,selectingbox,box10))
box11= Button(win, text="Box 11",height=3,width=14,command=lambda: boxclick(11,label,selectingbox,box11))
box12= Button(win, text="Box 12",height=3,width=14,command=lambda: boxclick(12,label,selectingbox,box12))
box13= Button(win, text="Box 13",height=3,width=14,command=lambda: boxclick(13,label,selectingbox,box13))
box14= Button(win, text="Box 14",height=3,width=14,command=lambda: boxclick(14,label,selectingbox,box14))
box15= Button(win, text="Box 15",height=3,width=14,command=lambda: boxclick(15,label,selectingbox,box15))

box1.grid(row=1,column=0)
box2.grid(row=1,column=1)
box3.grid(row=1,column=2)
box4.grid(row=1,column=3)
box5.grid(row=1,column=4)
box6.grid(row=2,column=0)
box7.grid(row=2,column=1)
box8.grid(row=2,column=2)
box9.grid(row=2,column=3)
box10.grid(row=2,column=4)
box11.grid(row=3,column=0)
box12.grid(row=3,column=1)
box13.grid(row=3,column=2)
box14.grid(row=3,column=3)
box15.grid(row=3,column=4)


win.mainloop()
