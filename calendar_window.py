import datetime
from tkcalendar import Calendar
from tkinter import *
from tkinter import ttk
import numpy as np
import calendar
from tkinter.ttk import *

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

count = 0
clicked_dates = ["" for i in range(31)]

def get_unique_values(some_list):
    unique_elements = []
    for i in some_list:
        if i not in unique_elements:
            unique_elements.append(i)
    return len(unique_elements) - 1



def get_date():
    global count
    data = cal.get_date()
    month, day, year = data.split("/")
    day = int(day)
    month = int(month)
    year = int(year) + 2000
    print(data)
    days = calendar.monthrange(int(year), int(month))
    print(days)
    clicked_dates[count] = data
    count = get_unique_values(clicked_dates)
    print(count)
    progress1 = count/days[1] * 100
    data = datetime.date(year,month,day)
    print("Progress: ", progress1)
    progress['value'] = int(progress1)
    progress.update_idletasks()
    cal.calevent_create(data, "", tags = "hi")

def click_date():
    get_date()
    cal.tag_config("hi", background = "red")

Button(progress_window, text="click_date",command=click_date).pack(pady=20)

date = Label(progress_window, text="")
date.pack(pady=20)

progress = Progressbar(progress_window, orient = HORIZONTAL,
              length = 100, mode = 'determinate')

progress.pack(pady = 10)

progress_window.mainloop()