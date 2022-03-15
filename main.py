from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk



class LogInWindow():  # login window

    def __init__(self):

        global login
        login = Tk()
        login.title("SetPy")
        login.resizable(0,0)
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
                NewMain()
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
            if messagebox.askyesno("Verify","Are you sure you want to logout?"):
                messagebox.showinfo("Please wait..", "Logging out..")
                newmain.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait...", "Navigating back..")
        def cr():
            newmain.destroy()
            Createplan()
# menus

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        createMenu = Menu(menu)
        createMenu.add_command(label="Create Plan", command=cr)
        menu.add_cascade(label="Create Plan", menu=createMenu)

        viewplannMenu = Menu(menu)
        viewplannMenu.add_command(label="View Plan")
        menu.add_cascade(label="View Plan", menu=viewplannMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="Help", command=HelpWindow)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_popbox)
        menu.add_cascade(label="Help", menu=helpMenu)


        self.text = Label(newmain, text="SetPy App", font=('Forte', 30), width=100, fg='black', bg='#ffd39b')
        self.text.pack(anchor=NW, ipady=5, padx=10, pady=10)


# entry(important)
# startentry

        self.text1 = Label(newmain, text="Start Date:", font=('Comic Sans MS', 12),fg='black')
        self.text1.place(anchor=NW, x=35, y=100)
        self.entry = Entry(newmain, font=('Comic Sans', 12), width=25,borderwidth=2)
        self.entry.place(x=145, y=106)
        self.text1 = Label(newmain, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        self.text1.place(x=235, y=130)

# endentry

        self.text1 = Label(newmain, text="End Date:", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=150)
        self.entry = Entry(newmain, font=('Comic Sans', 12), width=25,borderwidth=2)
        self.entry.place(x=145, y=156)
        self.text1 = Label(newmain, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        self.text1.place(x=235, y=180)

# starttime

        self.text1 = Label(newmain, text="Time of Sleep:(24 hours)", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=415)
        self.text1 = Label(newmain, text="Hour:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=45, y=460)
        self.text1 = Label(newmain, text="Minute:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=150, y=460)
        self.text1 = Label(newmain, text="Second:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=270, y=460)

        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=88, y=460)
        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=206, y=460)
        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=330, y=460)

# endtime

        self.text1 = Label(newmain, text="End of Sleep:(24 hours)", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=500)
        self.text1 = Label(newmain, text="Hour:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=45, y=545)
        self.text1 = Label(newmain, text="Minute:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=150, y=545)
        self.text1 = Label(newmain, text="Second:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=269, y=545)

        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=88, y=545)
        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=206, y=545)
        self.entry = Entry(newmain, font=('Comic Sans MS', 11), width=6, fg='black',borderwidth=2)
        self.entry.place(anchor=NW, x=330, y=545)

# calendar

        self.calendar = Calendar(newmain, selectmode= "day", year=2022, month=3, day=1)
        self.calendar.place(anchor=NW, x=121 ,y=210)

# Buttons
        self.button = Button(newmain ,width=10, bg='#ffd39b',fg='black', text='Submit', font=('Comic Sans MS',10),borderwidth=0, border=3)
        self.button.place(anchor=NW, x=80, y=600)
        self.label = Label(newmain, text="", width=90, height=3, bg='#ffd39b')
        self.label.place(anchor=NW, x=410, y=592)
        self.button = Button(newmain, width=10, bg='white', fg='black', text='Update', font=('Comic Sans MS', 10),
                             borderwidth=0, border=3)
        self.button.place(anchor=NW, x=480, y=600)
        self.button = Button(newmain, width=10, bg='white', fg='black', text='Delete', font=('Comic Sans MS', 10),
                             borderwidth=0, border=3)
        self.button.place(anchor=NW, x=600, y=600)
        self.button = Button(newmain, width=10, bg='white', fg='black', text='Clear All', font=('Comic Sans MS', 10),
                             borderwidth=0, border=3)
        self.button.place(anchor=NW, x=720, y=600)
        self.button = Button(newmain, width=16, bg='white', fg='black', text='View Improvements', font=('Comic Sans MS', 10),
                             borderwidth=0, border=3)
        self.button.place(anchor=NW, x=840, y=600)

# treeview

        text = Label(newmain, text="Sleep Data", font=('Comic Sans MS', 13), fg='black', bg='#ffd39b', width=60)
        text.place(anchor=NW, x=430, y=110)
        text = Label(newmain, text="", font=('Comic Sans MS', 13), fg='black', bg='#ffd39b', width=2, height=18)
        text.place(anchor=NW, x=410, y=110)
        text = Label(newmain, text="", font=('Comic Sans MS', 13), fg='black', bg='#ffd39b', width=2, height=18)
        text.place(anchor=NW, x=1020, y=110)
        text = Label(newmain, text="", font=('Comic Sans MS', 13), fg='black', bg='#ffd39b', width=63)
        text.place(anchor=NW, x=410, y=530)


        tablestyle = ttk.Style()
        tablestyle.theme_use("clam")
        tablestyle.configure("Treeview",
                             background = 'white',
                             foreground = 'black',
                             rowheight = 25,
                             fieldbackground = 'white'
                             )
        tablestyle.map("Treeview", background=[('selected','#ffd39b')])

        table = ttk.Treeview(newmain, height=15)

        table['columns'] = ("Start Date", "End Date","Start of Sleep", "End of Sleep", "Hours of Sleep", "Status")

        table.column('#0', width=0, stretch=NO)
        table.column('Start Date', anchor=W, width=90)
        table.column('End Date', anchor=W, width=90)
        table.column('Start of Sleep', anchor=W, width=100)
        table.column('End of Sleep', anchor=W, width=100)
        table.column('Hours of Sleep', anchor=W, width=110)
        table.column('Status', anchor=W, width=110)

        table.heading("#0", text="", anchor=W)
        table.heading("Start Date", text="Start Date", anchor=W)
        table.heading("End Date", text="End Date", anchor=W)
        table.heading("Start of Sleep", text="Start of Sleep", anchor=W)
        table.heading("End of Sleep", text="End of Sleep", anchor=W)
        table.heading("Hours of Sleep", text="Hours of Sleep", anchor=W)
        table.heading("Status", text="Status", anchor=W)
        table.place(anchor=NW, x=425, y=140)


        newmain.title("SetPy App")
        newmain.resizable(0,0)
        newmain.geometry("1080x700")
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

class Createplan():

    def __init__(self):

        create = Tk()

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Main Window.")

        def surelogout():
            if messagebox.askyesno("Verify","Are you sure you want to logout?"):
                messagebox.showinfo("Please wait..", "Logging out..")
                create.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait...", "Navigating back..")
        def back():
            create.destroy()
            NewMain()

        menu = Menu(create)
        create.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        createMenu = Menu(menu)
        createMenu.add_command(label="Main", command=back)
        menu.add_cascade(label="Main", menu=createMenu)

        viewplannMenu = Menu(menu)
        viewplannMenu.add_command(label="View Plan")
        menu.add_cascade(label="View Plan", menu=viewplannMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="Help", command=HelpWindow)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_popbox)
        menu.add_cascade(label="Help", menu=helpMenu)

# ENTRIES

        label = Label(create, text="SetPy App", font=('Forte', 30), fg='black', bg='#ffd39b', width=33)
        label.pack(anchor=NW, padx=10, pady=5)

        text = Label(create, text="Set Start Date:", font=('Comic Sans MS', 12), fg='black')
        text.place(anchor=NW, x=40, y=100)
        text = Label(create, text="Set End Date:", font=('Comic Sans MS', 12), fg='black')
        text.place(anchor=NW, x=40, y=170)
        text = Label(create, text="Set Start Time:", font=('Comic Sans MS', 12), fg='black')
        text.place(anchor=NW, x=40, y=240)
        text = Label(create, text="Set End Time:", font=('Comic Sans MS', 12), fg='black')
        text.place(anchor=NW, x=40, y=310)
        text1 = Label(create, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        text1.place(x=234, y=130)
        text1 = Label(create, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        text1.place(x=234, y=200)
        text1 = Label(create, text="H:M:S", font=('Comic Sans MS', 9), fg='black')
        text1.place(x=234, y=270)
        text1 = Label(create, text="H:M:S", font=('Comic Sans MS', 9), fg='black')
        text1.place(x=234, y=340)
        calendar = Calendar(create, selectmode="day", year=2022, month=3, day=1)
        calendar.place(anchor=NW, x=400, y=255)

        button = Button(create, text= "Create Plan", font=('Comic Sans MS', 12), fg='black', bg='#ffd39b', width=15, borderwidth=3)
        button.place(anchor=NW, x=70, y=400)

        entry = Entry(create, font=('Comic Sans MS', 13), fg='black', width=17)
        entry.place(anchor=NW, x=170, y=100)
        entry = Entry(create, font=('Comic Sans MS', 13), fg='black', width=17)
        entry.place(anchor=NW, x=170, y=170)
        entry = Entry(create, font=('Comic Sans MS', 13), fg='black', width=17)
        entry.place(anchor=NW, x=170, y=240)
        entry = Entry(create, font=('Comic Sans MS', 13), fg='black', width=17)
        entry.place(anchor=NW, x=170, y=310)

# treeview

        tablestyle = ttk.Style()
        tablestyle.theme_use("clam")
        tablestyle.configure("Treeview",
                             background='white',
                             foreground='black',
                             rowheight=25,
                             fieldbackground='white'
                             )
        tablestyle.map("Treeview", background=[('selected', '#ffd39b')])

        table = ttk.Treeview(create, height=4, selectmode="none")

        table['columns'] = ("Start Date", "End Date", "Start Time", "End Time")

        table.column('#0', width=0, stretch=NO)
        table.column('Start Date', anchor=W, width=62)
        table.column('End Date', anchor=W, width=61)
        table.column('Start Time', anchor=W, width=62)
        table.column('End Time', anchor=W, width=61)
        table.heading("#0", text="", anchor=W)
        table.heading("Start Date", text="Start Date", anchor=W)
        table.heading("End Date", text="End Date", anchor=W)
        table.heading("Start Time", text="Start Time", anchor=W)
        table.heading("End Time", text="End Time", anchor=W)
        table.place( anchor=NW, x=400, y=100)

        create.title("SetPy: Create your Own Sleep Schedule")
        create.geometry("700x500")
        create.resizable(0,0)
        create.mainloop()

    def about_popbox(self):
        about_input = "SETPy is an application that tracks and evaluate your sleeping routine.\
            \nIt will help you to track your sleeping hours and evaluate it if they are healthy or not.\
            \n Windows 10\
            \n Copyright 2022 Final Project 5"
        messagebox.showinfo("SETPy About", about_input)

LogInWindow()
