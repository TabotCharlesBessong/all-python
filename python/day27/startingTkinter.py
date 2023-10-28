
import  tkinter as t
 
window = t.Tk()
window.minsize(width=400,height=450)
window.title("My first GUI program")
label = t.Label(text="I am a good boy",font=("Helvetica",32,"bold"))
label.pack(side="left")


window.mainloop()