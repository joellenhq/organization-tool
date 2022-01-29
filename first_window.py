from tkinter import *
from tkinter import filedialog

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
    #print("login clicked!")
    user_found = False
    login_database = open("login_info.txt", "r")
    login_data = (username+","+password+"\n")
    for line in login_database:
        if line == login_data:
            user_found = True
            break
    if user_found:
        info = "login successful"
        user_window = Tk()
        window.destroy()    #close login window
    else:
        info = "wrong username or password"
    print(info)



def open_register_window():

    def register():
        username = r_username_entry.get()
        password = r_password_entry.get()
        password_confirmation = r_password_c_entry.get()
        login_database = open("login_info.txt", "r")

        if password == password_confirmation:
            if username in login_database:
                info = "username is already taken, try again"
            else:
                info = "registered successfully!"
                login_database = login_database = open("login_info.txt", "a")
                login_database.write(username + "," + password + "\n")
        else:
            info = "passwords do not match, try again"
        print(info)

    register_window = Toplevel()

    register_button_2 = Button(register_window,
                             text='register',
                             command=register,
                             bg='white',
                             activebackground='green',
                             bd=5,
                             fg='darkblue',
                             activeforeground='darkblue',
                             font=8,
                             state=ACTIVE)
    r_username_entry = Entry(register_window,
                           font=('Verdana', 12))
    r_password_c_entry = Entry(register_window,
                           font=('Verdana', 12),
                           show='*')
    r_password_entry = Entry(register_window,
                           font=('Verdana', 12),
                           show='*')

    r_username_entry.place(x=170, y=150)
    r_password_entry.place(x=170, y=180)
    r_password_c_entry.place(x=170, y=210)
    register_button_2.place(x=220, y=260)





register_button = Button(window,
                text = 'register',
                command = open_register_window(),
                bg = 'white',
                activebackground = 'green',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 8,
                state = ACTIVE)

login_button = Button(window,
                text = 'login',
                command = login,
                bg = 'white',
                activebackground = 'green',
                bd = 5,
                fg = 'darkblue',
                activeforeground = 'darkblue',
                font = 8,
                state = ACTIVE)

def enter_as_guest():
    guest_window = Toplevel()


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
                       font = ('Verdana',12))
password_entry = Entry(window,
                       font = ('Verdana',12),
                       show = '*')

username_entry.place(x = 170, y = 150)
password_entry.place(x = 170, y = 180)
login_button.place(x = 170, y = 210)
guest_button.place(x = 250, y = 210)
register_button.place(x = 220, y = 260)

window.mainloop()