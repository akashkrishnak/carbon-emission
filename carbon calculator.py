from tkinter import * 
from tkinter.ttk import *
master = Tk()
master.geometry("600x300")
master.resizable(False, False)
master.title("Carbon Emission Calculator of a Car")

def pr():
    res=(float(miles.get())/float(fuel.get()))*19.36/2204.6
    value=Label(master,text="                      ",font=50).place(x=350,y=220)
    value=Label(master,text=str(round(res,3))+" tons",font=50).place(x=350,y=220)
    if res>100:
        master.configure(bg="red")
    else:
        master.configure(bg="#f0f0f0")

miles=StringVar()
fuel=StringVar()
milesdriven=Label(master,text="Miles Driven :",font=50).place(x=60,y=50)
milesentry=Entry(master,width=30,textvariable=miles).place(x=300,y=52.5)
fuelefficiency=Label(master,text="Fuel Efficiency :",font=50).place(x=60,y=100)
fuelentry=Entry(master,width=30,textvariable=fuel).place(x=300,y=102.5)
calc=Button(text="Calculate",command=pr).place(x=250,y=175)
carbonemission=Label(master,text="Carbon Emission:",font=50).place(x=170,y=220)
value=Label(master,text="0",font=50).place(x=350,y=220)
mainloop()
