from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Organization tool")

icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

color_metallic_silver = '#BCC6CC'
window.config(background = color_metallic_silver)


label = Label(window,
              text = 'Choose an option!',
              font = ('Verdana',16,'bold'),
              fg = 'darkblue',
              bg = color_metallic_silver,
              relief = SUNKEN,
              bd = 4,
              padx = 4,
              pady = 10)

label.pack()

def see_calendar():
    pass
def see_tasks():
    pass
def see_progress():
    pass
def see_categories():
    pass


calendar_button = Button(window,
                text = 'calendar',
                command = see_calendar,
                bg = 'white',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 12,
                state = ACTIVE,
                padx = 18,
                pady = 16)

list_button = Button(window,
                text = 'list',
                command = see_tasks,
                bg = 'white',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 12,
                state = ACTIVE,
                padx = 38,
                pady = 16)

progress_button = Button(window,
                text = 'progress',
                command = see_progress,
                bg = 'white',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 12,
                state = ACTIVE,
                padx = 16,
                pady = 16)

categories_button = Button(window,
                text = 'categories',
                command = see_categories,
                bg = 'white',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 12,
                state = ACTIVE,
                padx = 10,
                pady = 16)

calendar_button.pack()
list_button.pack()
progress_button.pack()
categories_button.pack()

window.mainloop()