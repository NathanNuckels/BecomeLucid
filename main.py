from tkinter import *
import time
tk=Tk()
tk.geometry("1024x576")
tk.title("Lucid Tonight")

header_alarm=Label(tk)
text_time=Label(tk,text="Time:")
entry_hour=Entry(tk,width=5)
text_timeColon=Label(tk,text=":")
entry_minute=Entry(tk,width=5)
text_24time=Label(tk,text="Note: This uses 24 hour time")
button_feedback=Button(tk,text="Feedback") #,command=gitIssue)

header_alarm.grid(row=0,column=0)
text_time.grid(row=1,column=0)
entry_hour.grid(row=1,column=1)
text_timeColon.grid(row=1,column=2)
entry_minute.grid(row=1,column=3)
text_24time.grid(row=1,column=4)
while 1:
    tk.update()
    time.sleep(0.01)