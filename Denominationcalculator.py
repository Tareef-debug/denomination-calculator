from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("denomination counter")
root.configure(bg="light blue")
root.geometry("650x400")
label1=Label(root,text="Welcome to counter denomination app",bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msgbox = messagebox.showinfo("Alert,do you want to calculate denomination count?")
    if msgbox=="ok":
        topwind()
button1=Button(root,text="Lets get started",command = msg,bg="brown",fg="white")
button1.place(x=260,y=360)
def topwind():
    top = Toplevel()
    top.title("denomination calculator")
    top.configure(bg="light grey")
    top.geometry("600x350+50+50")
    label=Label(top,text="Enter total amount",bg = "light grey")
    entry=Entry(top)
    lbl=Label(top,text="Here are the number of notes for each denomination",bg="light grey")
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    d1=Entry(top)
    d2=Entry(top)
    d3=Entry(top)
    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note100=amount//100
            d1.delete(0,END)
            d2.delete(0,END)
            d3.delete(0,END)
            d1.insert(END,str(note2000))
            d2.insert(END,str(note500))
            d3.insert(END,str(note100))
        except ValueError:
            messagebox.showerror("error")
    btn=Button(top,text="Calculate",command=calculator,bg="brown",fg="white")
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    d1.place(x=270,y=200)
    d2.place(x=270,y=230)
    d3.place(x=270,y=260)
    top.mainloop()
root.mainloop()