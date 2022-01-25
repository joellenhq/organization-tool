from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Organization tool")

color_metallic_silver = '#BCC6CC'
window.config(background = color_metallic_silver)

icon = PhotoImage(file='icon.png')
window.iconphoto(True, icon)

welcome_text = 'This is a tool to help you manage time!'
label = Label(window,
              text = welcome_text,
              font = ('Verdana',10,'bold'),
              fg = 'darkblue',
              bg = color_metallic_silver,
              relief = SUNKEN,
              bd = 4,
              padx = 4,
              pady = 10)

label.place(x = 120, y = 100)

def login():
    username = username_entry.get()
    password = password_entry.get()
    print("login clicked!")

login_button = Button(window,
                text = 'login',
                command = login,
                bg = 'white',
                activebackground = 'green',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 8,
                state = DISABLED)

def enter_as_guest():
    pass

guest_button = Button(window,
                text = 'login as guest',
                command = enter_as_guest,
                bg = 'white',
                activebackground = 'green',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 8,
                state = ACTIVE)

username_entry = Entry(window,
                       font = ('Verdana',12),)
password_entry = Entry(window,
                       font = ('Verdana',12),
                       show = '*')

username_entry.place(x = 170, y = 150)
password_entry.place(x = 170, y = 180)
login_button.place(x = 170, y = 210)
guest_button.place(x = 250, y = 210)

window.mainloop()