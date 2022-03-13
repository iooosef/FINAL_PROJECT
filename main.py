from tkinter import *
from tkinter import messagebox



class LogInWindow():  # login window

    def __init__(self):

        global login
        login = Tk()
        login.title("SetPy")
        login.geometry("400x400")

        self.menu1 = Menu(login)
        login.config(menu=self.menu1)

        def log():

            user = username.get()
            passw = password.get()

            if user == "" and passw == "":
                messagebox.showinfo("Warning!", "Please fill the required fields!")
            elif user == "Admin" and passw == "admin123":
                messagebox.showinfo("Please Wait..", "Logging In...")
                login.destroy()
                new_window = NewMain()
            else:
                messagebox.showinfo("Warning!", "Invalid!")

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Login Menu.")

        file_menu = Menu(self.menu1)
        self.menu1.add_cascade(label="Options", menu=file_menu)
        file_menu.add_command(label="Help", command=HelpWindow)
        file_menu.add_command(label="Quit", command=surequit)

        self.text = Label(login, text="SetPy", font=('Forte', 34), fg='black', bg='#FFD39B', width=60)
        self.text.pack(ipady=50, pady=10, padx=10)

        global username
        global password

        username = StringVar()
        password = StringVar()

        self.label = Label(login, text="Username:", font=('Arial', 12), fg='black').place(x=40, y=200)
        self.entry1 = Entry(login, textvariable=username, font=('Comic Sans MS', 10), fg='black', width=26,
                            borderwidth=3)
        self.entry1.place(x=140, y=200)
        self.label = Label(login, text="Password:", font=('Arial', 12), fg='black').place(x=40, y=240)
        self.entry2 = Entry(login, textvariable=password, font=('Comic Sans MS', 10), fg='black', width=26,
                            borderwidth=3,
                            show="*")
        self.entry2.place(x=140, y=240)
        self.button1 = Button(login, text="Log In", font=('Arial', 11), bg='#FFD39B', width=12, borderwidth=2,
                              command=log, height=1).place(x=150, y=290)

        login.mainloop()


class NewMain(Frame):

    def __init__(self):
        newmain = Tk()
        menu = Menu(newmain)
        newmain.config(menu=menu)

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Main Window.")

        def surelogout():
            if messagebox.showwarning("Verify","Are you sure you want to logout?"):
                newmain.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait", "Navigating back..")

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        createMenu = Menu(menu)
        createMenu.add_command(label="Create Plan")
        menu.add_cascade(label="Create Plan", menu=createMenu)

        viewplannMenu = Menu(menu)
        viewplannMenu.add_command(label="View Plan")
        menu.add_cascade(label="View Plan", menu=viewplannMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="Help", command=HelpWindow)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_popbox)
        menu.add_cascade(label="Help", menu=helpMenu)

        newmain.title("SetPy App")
        newmain.geometry("700x500")
        newmain.mainloop()

    def about_popbox(self):
        about_input = "SETPy is an application that tracks and evaluate your sleeping routine.\
            \nIt will help you to track your sleeping hours and evaluate it if they are healthy or not.\
            \n Windows 10\
            \n Copyright 2022 Final Project 5"
        messagebox.showinfo("SETPy About", about_input)


class HelpWindow():

    def __init__(self):
        help = Tk()  # ongoing edit

        self.button = Button(help, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2, command=help.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.text3 = Label(help, text="How to use SetPy?", font=('Comic Sans MS', 15), fg='black', bg='#ffd39b', width=50)
        self.text3.pack(ipady=30, padx=10, pady=5)
        help_input = "1. Raiden Shogun\
            \n2. Shenhe\
            \n3. Ningguang\
            \n5. Kaedahara Kazuha\
            \n6. Venti\
            \n7. Kamisato Ayato"
        msg = Message(help, text=help_input)
        msg.config(justify="left", font=('arial', 22))
        msg.pack()
        help.title("Help")
        help.geometry("400x500")
        help.mainloop()


LogInWindow()
