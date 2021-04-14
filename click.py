from tkinter import *

window=Tk()
window.geometry("400x400")
txt=Entry(window, width=20)
txt.grid(row=1, column=0)
lbl=Label(window, text="Say anything", font=15)
lbl.grid(row=0, column=0)
lbl2=Label(window)
lbl2.grid(row=3, column=0)
def click():
    res="Say this + " + txt.get()
    lbl2.configure(text=res, font=15)

btn=Button(window, text="Enter", command=click)
btn.grid(row=2, column=0)
window.mainloop()