from tkinter import *
from tkinter import ttk
import time
import os

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
        user_window.geometry("500x500")
        user_window.title("Organization tool")

        label = Label(user_window,
                      text='Choose an option!',
                      font=('Verdana', 16, 'bold'),
                      fg='darkblue',
                      bg=color_metallic_silver,
                      relief=SUNKEN,
                      bd=4,
                      padx=4,
                      pady=10)

        label.pack()

        def set_timer():

            def start_counting():
                minutes_to_count = int(minutes.get())
                if minutes_to_count > 0 and minutes_to_count < 60:
                    info = "proper settings"
                    start = time.time()
                    end = time.time()
                    difference = (start - end)/60
                    while abs(difference) < minutes_to_count:
                        end = time.time()
                        difference = (start - end)/60
                        print(difference)
                        #improve -> set frequency of the loop

                    info = "time has passed"
                else:
                    info = "wrong time settings"
                print(info)

            timer_window = Toplevel()
            minutes = Entry(timer_window,
                       font = ('Verdana',12))
            start_timer = Button(timer_window,
                                 text='timer',
                                 command=start_counting,
                                 bg='white',
                                 bd=5,
                                 fg='darkblue',
                                 activeforeground='darkblue',
                                 font=12,
                                 state=ACTIVE,
                                 padx=18,
                                 pady=16)
            minutes.pack()
            start_timer.pack()



        def see_tasks():
            task_window = Toplevel()

        def see_progress():
            progress_window = Toplevel()
            notebook = ttk.Notebook(progress_window)
            tab1 = Frame(notebook)
            tab2 = Frame(notebook)

            notebook.add(tab1, text="task1")
            notebook.add(tab2, text="task2")
            notebook.pack(expand=True, fill="both")

            task1_label = Label(tab1, text="see progress of task1").pack()
            task2_label = Label(tab2, text="see progress of task2").pack()

            #grid widget in a loop could be good idea


        def see_categories():
            categories_window = Toplevel()

            file = username+".txt"
            if not os.path.exists(file):
                with open(file, 'w'): pass

        timer_button = Button(user_window,
                                 text='timer',
                                 command=set_timer,
                                 bg='white',
                                 bd=5,
                                 fg='darkblue',
                                 activeforeground='darkblue',
                                 font=12,
                                 state=ACTIVE,
                                 padx=30,
                                 pady=16)

        list_button = Button(user_window,
                             text='list',
                             command=see_tasks,
                             bg='white',
                             bd=5,
                             fg='darkblue',
                             activeforeground='darkblue',
                             font=12,
                             state=ACTIVE,
                             padx=38,
                             pady=16)

        progress_button = Button(user_window,
                                 text='progress',
                                 command=see_progress,
                                 bg='white',
                                 bd=5,
                                 fg='darkblue',
                                 activeforeground='darkblue',
                                 font=12,
                                 state=ACTIVE,
                                 padx=16,
                                 pady=16)

        categories_button = Button(user_window,
                                   text='categories',
                                   command=see_categories,
                                   bg='white',
                                   bd=5,
                                   fg='darkblue',
                                   activeforeground='darkblue',
                                   font=12,
                                   state=ACTIVE,
                                   padx=10,
                                   pady=16)

        timer_button.pack()
        list_button.pack()
        progress_button.pack()
        categories_button.pack()


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
            elif len(username)==0 or len(password)<3 or len(password_confirmation)<3:
                info = "wrong registration data"
            else:
                info = "registered successfully!"
                login_database = open("login_info.txt", "a")
                login_database.write(username + "," + password + "\n")
        else:
            info = "passwords do not match, try again"
        print(info)

    register_window = Toplevel()
    register_window.geometry("400x400")

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
                #activebackground = 'green',
                bd = 5,
                fg = 'darkblue',
                #activeforeground = 'darkblue',
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