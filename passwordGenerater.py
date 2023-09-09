from tkinter import *
import string
import random
def genPassword():
    radiovalue=var.get()
    slidervalue=myslider.get()
    s1=string.ascii_letters
    s2=string.digits
    s3=string.punctuation
    if radiovalue==1:
        value.set("".join(random.sample(s1,slidervalue)))
    if radiovalue==2:
        s=[]
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        value.set("".join(random.sample(s,slidervalue)))
windows=Tk()
windows.geometry("444x444")
var=IntVar()
Label(windows,text="Password Type",font="lucida 20 bold").pack()
radio=Radiobutton(windows,text="Basic",variable=var,value=1,font="lucida 15 ").pack()
radio=Radiobutton(windows,text="Strong",variable=var,value=2,font="lucida 15 ").pack()
Label(windows,text="Password Size",font="lucida 20 bold").pack()
myslider=Scale(windows,from_=8,to=20,font="lucida 15",orient=HORIZONTAL)
myslider.pack()
Button(windows,text="Submit",command=genPassword,padx=25,pady=10,font="lucida 15 bold",bg="grey").pack(padx=25,pady=35)
value=StringVar()
value.set("")
display=Entry(windows,textvar=value,font=("serif 20 bold"))
display.pack(fill=X,ipadx=20,ipady=20,padx=10)
windows.mainloop()