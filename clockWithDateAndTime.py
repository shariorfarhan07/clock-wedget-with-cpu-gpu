from tkinter import *
import time
from datetime import date
from datetime import datetime
from PIL import ImageTk, Image

window = Tk()
window.title("Farhans widget")
#  set size of the widget window
window.geometry("400x200-0-0")
# set color of the background of the window
window.config(bg="#add123")
# fixed the window on the top of the screen
window.attributes('-topmost', True)
#make the background color transparent
window.wm_attributes("-transparentcolor", "#add123")
window.overrideredirect(True)
# this lables are for displaying time
timelabel = Label(window, fg="white", bg="#add123", font=("Lucida", 45))
dateLabel = Label(window,  fg="white", bg="#add123", font=("Lucida", 22))

frame = Frame(window, width=400, height=100,bg="#add123")
def Update():
    global date, datetime , timelabel, dateLabel ,window ,frame
    date = date.today()
    now = datetime.now()
    time = now.strftime("%I:%M:%S %p")
    formatDate=now.strftime("%a %d %B %Y")
    timelabel['text']=time
    dateLabel['text']=formatDate
    timelabel.pack()
    dateLabel.pack()
    frame.pack()
    window.after(1000, Update)


Update()
window.mainloop()