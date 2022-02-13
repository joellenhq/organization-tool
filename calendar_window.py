import datetime

from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk

progress_window = Toplevel()
progress_window.geometry("500x500")

notebook = ttk.Notebook(progress_window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="task1")
notebook.add(tab2, text="task2")
notebook.pack(expand=True, fill="both")

task1_label = Label(tab1, text="see progress of task1").pack()
task2_label = Label(tab2, text="see progress of task2").pack()


cal = Calendar(progress_window, selectmode='day',
               year=2022, month=2,
               day=13)

cal.pack(pady=20, fill="both", expand=True)



def click_date():
    data = cal.get_date()
    month, day, year = data.split("/")
    day = int(day)
    month = int(month)
    year = int(year) + 2000
    print(data)

    data = datetime.date(year,month,day)
    print(data)
    cal.calevent_create(data, "", tags = "hi")
    cal.tag_config("hi", background = "red")
    #self.buttonA.confi, gure(bg="yellow")



# Adding the Button and Label
Button(progress_window, text="click_date",command=click_date).pack(pady=20)

date = Label(progress_window, text="")
date.pack(pady=20)

progress_window.mainloop()