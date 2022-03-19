from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from datetime import date


class LogInWindow():  # login window

    def __init__(self):

        global login
        login = Tk()
        login.title("SetPy")
        login.resizable(0, 0)
        login.geometry("400x400")

        self.menu1 = Menu(login)
        login.config(menu=self.menu1)

        def log(event=None):
            user = username.get()
            passw = password.get()
            if user == "" and passw == "":
                messagebox.showinfo("Warning!", "Please fill the required fields!")
            elif user == "Admin" and passw == "admin123":
                login.withdraw()
                try:
                    login.after(800, login.destroy)
                    messagebox.showinfo('Please Wait..', "Logging In...", master=login)
                except:
                    pass
                new_window = NewMain()
                NewMain()
            else:
                messagebox.showinfo("Warning!", "Invalid!")

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Login Menu.")

        file_menu = Menu(self.menu1, tearoff=FALSE)
        self.menu1.add_cascade(label="Options", menu=file_menu)

        self.submenu = Menu(file_menu, tearoff=FALSE)
        self.submenu.add_command(label="Login", command=ImageWindow_Login)
        self.submenu.add_command(label="Menu", command=ImageWindow_Menu)
        self.submenu.add_command(label="Sleep Tracker", command=ImageWindow_SleepTracker)
        self.submenu.add_command(label="Create Plan", command=ImageWindow_CreatePlan)
        self.submenu.add_command(label="Sleep Data", command=ImageWindow_SleepData)
        self.submenu.add_command(label="Sleep Data Features", command=ImageWindow_SleepDataFeatures)
        self.submenu.add_command(label='Summarry', command=HelpWindow)

        file_menu.add_cascade(label="Help", menu=self.submenu)
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
        login.bind('<Return>', log)
        login.mainloop()


class NewMain(Frame):
    def __init__(self):
        newmain = Tk()
        menu = Menu(newmain, tearoff=FALSE)
        newmain.config(menu=menu)

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Main Window.")

        def surelogout():
            if messagebox.askyesno("Verify", "Are you sure you want to logout?"):
                messagebox.showinfo("Please wait..", "Logging out..")
                newmain.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait...", "Navigating back..")

        def cr():
            newmain.destroy()
            Createplan()

        def vp():
            newmain.destroy()
            ViewPlan()

        # menus

        fileMenu = Menu(menu, tearoff=FALSE)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        createMenu = Menu(menu, tearoff=FALSE)
        createMenu.add_command(label="Create Plan", command=cr)
        menu.add_cascade(label="Create Plan", menu=createMenu)

        viewplannMenu = Menu(menu, tearoff=FALSE)
        viewplannMenu.add_command(label="View Plan", command=vp)
        menu.add_cascade(label="View Plan", menu=viewplannMenu)

        helpMenu = Menu(menu, tearoff=FALSE)
        helpMenu.add_command(label="Help", command=HelpWindow)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_popbox)
        menu.add_cascade(label="Help", menu=helpMenu)

        self.text = Label(newmain, text="SetPy App", font=('Forte', 30), width=100, fg='black', bg='#ffd39b')
        self.text.pack(anchor=NW, ipady=5, padx=10, pady=10)

        # entry(important)
        def evaluation():

            global hour1
            global hour2

            h1 = int(hour1.get())
            h2 = int(hour2.get())
            m1 = int(min1.get())
            m2 = int(min2.get())
            s1 = int(sec1.get())
            s2 = int(sec2.get())

            hour1 = float((h1) + (m1 / 60) + (s1 / 60))
            hour2 = float((h2) + (m2 / 60) + (s2 / 60))

            sleephours = (24 - hour1) + hour2

            if 8 >= sleephours or sleephours <= 9:
                Label(newmain, text="Good").pack()
                messagebox.showinfo(title="Message", message="Keep Up The Good Sleeping Habit! It will help you maintain your health and improve your\
                                                            immune system to protect you from every kind of sickness. For more information, search for the 'The Benefits of Getting a Full Night's Sleep' by 'SCL Health' page.")
            elif 10 >= sleephours:
                Label(newmain, text="Excellent").pack()
                messagebox.showinfo(title="Message", message="Keep Up The Good Sleeping Habit! It will help you maintain your health and improve your\
                                                            immune system to protect you from every kind of sickness. For more information, search for the 'The Benefits of Getting a Full Night's Sleep' by 'SCL Health' page.")
            elif sleephours <= 11:
                Label(newmain, text="Too much").pack()
                messagebox.showinfo(title="Message", message="Please avoid sleeping too much. Too much is dangerous for your health! Even though sleep is essential,\
                                                            it is not good for your helth to sleep for a long period of time. It will destroy our health balance that may lead to degrading our immune system.\
                                                            For more information, search for the 'Oversleeping: The Effects & Health Risks of Sleeping Too Much' by 'Amerisleep' page.")
            else:
                Label(newmain, text="Need Improvement").pack()
                messagebox.showinfo(title="Message", message="Please Track your Habits and Rest More! This kind of habits will degrade your health and immune system.\
Lack of Sleep will destroy your health balance and the strength of your immune system. For more information, \
search for the 'What Happens When You Don't Get Enough Sleep' by 'Cleveland Clinic' page.")

       # startentry
        self.text1 = Label(newmain, text="Start Date:", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=100)
        self.entry_startdate = ttk.Entry(newmain, font=('Comic Sans', 12), width=25)
        self.entry_startdate.place(x=145, y=106)
        self.text1 = Label(newmain, text="M|D|Y", font=('Comic Sans MS', 9), fg='black')
        self.text1 = Label(newmain, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        self.text1.place(x=235, y=130)

        # endentry
        self.text1 = Label(newmain, text="End Date:", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=150)
        self.entry_enddate = ttk.Entry(newmain, font=('Comic Sans', 12), width=25)
        self.entry_enddate.place(x=145, y=156)
        self.text1 = Label(newmain, text="M|D|Y", font=('Comic Sans MS', 9), fg='black')
        self.text1 = Label(newmain, text="M/D/Y", font=('Comic Sans MS', 9), fg='black')
        self.text1.place(x=235, y=180)

        # highlight focus startentry or endentry
        styleEntry = ttk.Style()
        styleEntry.theme_use('clam')
        styleEntry.map('TEntry', lightcolor=[('focus', 'green')])

        self.entry_startdate.bind('<Button-1>', lambda e: pick_date(e, self.entry_startdate))
        self.entry_enddate.bind('<Button-1>', lambda e: pick_date(e, self.entry_enddate))

        # calendar
        date_today = date.today()
        self.calendar = Calendar(newmain, selectmode="day", 
                                    year=int(date_today.strftime("%Y")), 
                                    month=int(date_today.strftime("%m")), 
                                    day=int(date_today.strftime("%d")))
        self.calendar.place(anchor=NW, x=110, y=210)
        # get date calendar
        def pick_date(event, entry_date):
            entry_date.delete(0, END)
            entry_date.insert(0, self.calendar.get_date())

        global hour1
        global min1
        global sec1

        global hour2
        global min2
        global sec2
        hour1 = StringVar()
        min1 = StringVar()
        sec1 = StringVar()
        hour2 = StringVar()
        min2 = StringVar()
        sec2 = StringVar()

        # starttime
        self.text1 = Label(newmain, text="Time of Sleep:(24 hours)", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=415)
        self.text1 = Label(newmain, text="Hour:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=45, y=460)
        self.text1 = Label(newmain, text="Minute:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=150, y=460)
        self.text1 = Label(newmain, text="Second:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=270, y=460)
        self.hours_start = Entry(newmain, textvariable=hour1, font=('Comic Sans MS', 11), width=6, fg='black',
                                 borderwidth=2)
        self.hours_start.place(anchor=NW, x=88, y=460)
        self.minutes_start = Entry(newmain, textvariable=min1, font=('Comic Sans MS', 11), width=6, fg='black',
                                   borderwidth=2)
        self.minutes_start.place(anchor=NW, x=206, y=460)
        self.seconds_start = Entry(newmain, textvariable=sec1, font=('Comic Sans MS', 11), width=6, fg='black',
                                   borderwidth=2)
        self.seconds_start.place(anchor=NW, x=330, y=460)

        # endtime
        self.text1 = Label(newmain, text="End of Sleep:(24 hours)", font=('Comic Sans MS', 12), fg='black')
        self.text1.place(anchor=NW, x=35, y=500)
        self.text1 = Label(newmain, text="Hour:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=45, y=545)
        self.text1 = Label(newmain, text="Minute:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=150, y=545)
        self.text1 = Label(newmain, text="Second:", font=('Comic Sans MS', 10), fg='black')
        self.text1.place(anchor=NW, x=269, y=545)
        self.hours_end = Entry(newmain, textvariable=hour2, font=('Comic Sans MS', 11), width=6, fg='black',
                               borderwidth=2)
        self.hours_end.place(anchor=NW, x=88, y=545)
        self.minutes_end = Entry(newmain, textvariable=min2, font=('Comic Sans MS', 11), width=6, fg='black',
                                 borderwidth=2)
        self.minutes_end.place(anchor=NW, x=206, y=545)
        self.seconds_end = Entry(newmain, textvariable=sec2, font=('Comic Sans MS', 11), width=6, fg='black',
                                 borderwidth=2)
        self.seconds_end.place(anchor=NW, x=330, y=545)

        # Buttons
        self.button = Button(newmain, width=10, bg='#ffd39b', fg='black', text='Submit', font=('Comic Sans MS', 10),
                             borderwidth=0, border=3, command=evaluation)
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
        self.button = Button(newmain, width=16, bg='white', fg='black', text='View Improvements',
                             font=('Comic Sans MS', 10),
                             borderwidth=0, border=3, command=ViewImprovements)
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
                             background='white',
                             foreground='black',
                             rowheight=25,
                             fieldbackground='white'
                             )
        tablestyle.map("Treeview", background=[('selected', 'grey')])
        table = ttk.Treeview(newmain, height=15)
        table['columns'] = ("Start Date", "End Date", "Start of Sleep", "End of Sleep", "Hours of Sleep", "Status")
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
        
        # Adding Data (Temp)
        table.insert("", 'end', iid=0, values=("3/15/2022", "3/16/2022", "10:30:00", "9:30:00", "11", "Good"))
        table.pack(pady=20)

        table.place(anchor=NW, x=425, y=140)
        newmain.title("SetPy App")
        newmain.resizable(0, 0)
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
        help = Tk()
        self.button = Button(help, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=help.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.text3 = Label(help, text="How to use SetPy?", font=('Comic Sans MS', 15), fg='black', bg='#ffd39b',
                           width=50)
        self.text3.pack(ipady=30, padx=10, pady=5)
        help_input = " 1.  To access the application, enter Admin in the Username section then, enter admin123 for the password section.\
            \n 2.  On the main page, you can create and view your sleep schedule.\
            \n 3. On the left side of the main window, you can input the time you started sleeping as well as the time you woke up. \
This section will be the basis of the data and will be used to evaluate your sleeping hours for the day.\
The data will be recorded in the Sleep Data section of the main window.\
            \n 4. To create your own sleeping schedule, press the Create Plan found in the Menu of the application.\
Set the time and data in order to create it.\
            \n 5. Back to the main page, the Sleep Data section would be the data records of the schedule created. \
You can delete and edit the recorded schedule.\
            \n 6. When the scheduled plan is accomplished, it will be also recorded in the Sleep Data Section. \
You can also delete the activity history for an organized look in this section of the main page."
        msg = Text(help, height=50, width=50, font=("comic sans ms", 12))
        msg.pack(fill=Y, padx=15, pady=15)
        msg.insert(END, help_input)

        help.title("Help")
        help.geometry("450x550")
        scroll = Scrollbar(help)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=msg.yview)
        msg.config(yscrollcommand=scroll.set)
        help.mainloop()


class ImageWindow_Login():
    def __init__(self):
        self.root = Tk()
        helpinput = "To access the application, enter Admin in the Username section then, enter admin123 for the password section."
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Login")
        self.root.geometry("230x180")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open("oop1.png")
        resized_logo1 = logo1_open.resize((400, 400), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


class ImageWindow_Menu():
    def __init__(self):
        self.root = Tk()
        helpinput = "On the main page, you can create and view your sleep schedule."
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Menu")
        self.root.geometry("200x140")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open("oop2.png")
        resized_logo1 = logo1_open.resize((400, 100), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


class ImageWindow_SleepTracker():
    def __init__(self):
        self.root = Tk()
        helpinput = "On the left side of the main window, you can input the time you started sleeping as well as the time you woke up. \
This section will be the basis of the data and will be used to evaluate your sleeping hours for the day. \
The data will be recorded in the Sleep Data section of the main window."
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Sleep Tracker")
        self.root.geometry("350x250")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open(r"C:\Users\emtac\Documents\Code (MS Visual Studio)\project\oop1.png")
        resized_logo1 = logo1_open.resize((400, 400), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


class ImageWindow_CreatePlan():
    def __init__(self):
        self.root = Tk()
        helpinput = "To create your own sleeping schedule, press the Create Plan found in the Menu of the application. \
Set the time and data in order to create it"
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Create Plan")
        self.root.geometry("300x200")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open(r"C:\Users\emtac\Documents\Code (MS Visual Studio)\project\oop1.png")
        resized_logo1 = logo1_open.resize((400, 400), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


class ImageWindow_SleepData():
    def __init__(self):
        self.root = Tk()
        helpinput = "To create your own sleeping schedule, press the Create Plan found in the Menu of the application. \
Set the time and data in order to create it"
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Sleep Data")
        self.root.geometry("300x200")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open(r"C:\Users\emtac\Documents\Code (MS Visual Studio)\project\oop1.png")
        resized_logo1 = logo1_open.resize((400, 400), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


class ImageWindow_SleepDataFeatures():
    def __init__(self):
        self.root = Tk()
        helpinput = " When the scheduled plan is accomplished, it will be also recorded in the Sleep Data Section. \
You can also delete the activity history for an organized look in this section of the main page."
        mssg1 = Message(self.root, text=helpinput)
        mssg1.config(bg="#FEDEBE", font=("comic sans ms", 13))
        self.root.title("Sleep Data Features")
        self.root.geometry("300x210")
        self.button = Button(self.root, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=self.root.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        mssg1.pack()

        img = Toplevel()
        logo1_open = Image.open(r"C:\Users\emtac\Documents\Code (MS Visual Studio)\project\oop1.png")
        resized_logo1 = logo1_open.resize((400, 400), Image.ANTIALIAS)
        logo1 = ImageTk.PhotoImage(resized_logo1)
        step1 = Label(img, image=logo1, width=400, height=400)
        step1.pack()
        img.title("Instructions")
        self.button = Button(img, text="Go back", font=('Arial', 7), fg='black', width=9, borderwidth=2,
                             command=img.destroy)
        self.button.pack(anchor='nw', pady=1, padx=5)
        self.root.mainloop()


 # view improvement window

class ViewImprovements():

    def __init__(self):

        improvements = Tk()

        button = Button(improvements, text="Go back", width=10, borderwidth=1, fg='black', command=improvements.destroy)
        button.place(anchor=NW, x=3, y=3)
         # mydata =  #object for the data base
        # mycursor = #mydata.cursor()

        # mycursor.execute("dates", "sleeping hours")
        # result = mycursor.fetchall

        # Dates = []
        # SleepHours = []

        # for i in mycursor:
        # Dates.append(i[0])
        # SleepHours.append(i[1])

        # print("Dates = ", Dates)
        # print("Sleep Hours = ", SleepHours)

        # plt.plot(Dates, SleepHours)
        # plt.ylim(0,15)
        # plt.xlabel("Dates")
        # plt.tlabel("Sleep Hours")
        # plt.title("Sleep Hours Data Graph")
        # plt.show

        improvements.title("SetPy: View Improvements")
        improvements.geometry("700x500")
        improvements.resizable(0,0)
        improvements.mainloop()

# view plan window

class ViewPlan():  # Data Graph
    def __init__(self):
        view = Tk()

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Main Window.")

        def surelogout():
            if messagebox.askyesno("Verify", "Are you sure you want to logout?"):
                messagebox.showinfo("Please wait..", "Logging out..")
                view.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait...", "Navigating back..")

        def back():
            view.destroy()
            NewMain()

        def back2():
            view.destroy()
            Createplan()

        menu = Menu(view)
        view.config(menu=menu)

        fileMenu = Menu(menu, tearoff=FALSE)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        mainMenu = Menu(menu, tearoff=FALSE)
        mainMenu.add_command(label="Main", command=back)
        menu.add_cascade(label="Main", menu=mainMenu)

        createMenu = Menu(menu, tearoff=FALSE)
        createMenu.add_command(label="Create Plan", command=back2)
        menu.add_cascade(label="Create Plan", menu=createMenu)

        helpMenu = Menu(menu, tearoff=FALSE)
        helpMenu.add_command(label="Help", command=HelpWindow)
        helpMenu.add_separator()
        helpMenu.add_command(label="About", command=self.about_popbox)
        menu.add_cascade(label="Help", menu=helpMenu)

# treeview

        label = Label(view, text="SetPy App", font=('Forte', 30), fg='black', bg='#ffd39b', width=33)
        label.pack(anchor=NW, padx=10, pady=5)

        tablestyle = ttk.Style()
        tablestyle.theme_use("clam")
        tablestyle.configure("Treeview",
                             background='white',
                             foreground='black',
                             rowheight=25,
                             fieldbackground='white'
                             )
        tablestyle.map("Treeview", background=[('selected', 'grey')])

        table = ttk.Treeview(view, height=8)

        table['columns'] = ("Start Date", "End Date", "Start Time", "End Time")

        table.column('#0', width=0, stretch=NO)
        table.column('Start Date', anchor=W, width=146)
        table.column('End Date', anchor=W, width=146)
        table.column('Start Time', anchor=W, width=146)
        table.column('End Time', anchor=W, width=146)
        table.heading("#0", text="", anchor=W)
        table.heading("Start Date", text="Start Date", anchor=W)
        table.heading("End Date", text="End Date", anchor=W)
        table.heading("Start Time", text="Start Time", anchor=W)
        table.heading("End Time", text="End Time", anchor=W)
        table.place(anchor=NW, x=50, y=60)

#  entries and buttons

        label = Label(view, text="Start Date:", font=('Comic Sans MS',12), fg='black')
        label.place(anchor=NW, x=45, y=300)
        label = Label(view, text="End Date:", font=('Comic Sans MS', 12), fg='black')
        label.place(anchor=NW, x=45, y=340)
        label = Label(view, text="Start Time:", font=('Comic Sans MS', 12), fg='black')
        label.place(anchor=NW, x=45, y=380)
        label = Label(view, text="End Time:", font=('Comic Sans MS', 12), fg='black')
        label.place(anchor=NW, x=45, y=420)

        entry = Entry(view, font=('Comic Sans MS', 12), width=30)
        entry.place(x=140, y=300)
        entry = Entry(view, font=('Comic Sans MS', 12), width=30)
        entry.place(x=140, y=340)
        entry = Entry(view, font=('Comic Sans MS', 12), width=30)
        entry.place(x=140, y=380)
        entry = Entry(view, font=('Comic Sans MS', 12), width=30)
        entry.place(x=140, y=420)

        button = Button(view, text="Update", font=('Comic Sans MS', 12), fg='black', bg='#ffd39b', width=10, borderwidth=3)
        button.place(x=500, y=310)
        button = Button(view, text="Delete", font=('Comic Sans MS', 12), fg='black', bg='#ffd39b', width=10,
                        borderwidth=3)
        button.place(x=500, y=355)
        button = Button(view, text="Clear All", font=('Comic Sans MS', 12), fg='black', bg='#ffd39b', width=10,
                        borderwidth=3)
        button.place(x=500, y=400)

        view.title("SetPy: View Your Sleep Schedule")
        view.geometry("700x500")
        view.resizable(0,0)
        view.mainloop()

    def about_popbox(self):
        about_input = "SETPy is an application that tracks and evaluate your sleeping routine.\
            \nIt will help you to track your sleeping hours and evaluate it if they are healthy or not.\
            \n Windows 10\
            \n Copyright 2022 Final Project 5"
        messagebox.showinfo("SETPy About", about_input)

        
        
# create plan window

class Createplan():

    def __init__(self):

        create = Tk()

        def surequit():
            if messagebox.askyesno("Verify", "Are you sure you want to quit?"):
                exit()
            else:
                messagebox.showinfo("Return", "User will return to the Main Window.")

        def surelogout():
            if messagebox.askyesno("Verify", "Are you sure you want to logout?"):
                messagebox.showinfo("Please wait..", "Logging out..")
                create.destroy()
                LogInWindow()
            else:
                messagebox.showinfo("Please wait...", "Navigating back..")

        def back():
            create.destroy()
            NewMain()

        def back2():
            create.destroy()
            ViewPlan()

        menu = Menu(create)
        create.config(menu=menu)

        fileMenu = Menu(menu, tearoff=FALSE)
        fileMenu.add_command(label="Logout", command=surelogout)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=surequit)
        menu.add_cascade(label="File", menu=fileMenu)

        mainMenu = Menu(menu, tearoff=FALSE)
        mainMenu.add_command(label="Main", command=back)
        menu.add_cascade(label="Main", menu=mainMenu)

        viewplannMenu = Menu(menu, tearoff=FALSE)
        viewplannMenu.add_command(label="View Plan", command=back2)
        menu.add_cascade(label="View Plan", menu=viewplannMenu)

        helpMenu = Menu(menu, tearoff=FALSE)
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

        button = Button(create, text="Create Plan", font=('Comic Sans MS', 12), fg='black', bg='#ffd39b', width=15,
                        borderwidth=3)
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
        table.place(anchor=NW, x=400, y=100)

        create.title("SetPy: Create your Own Sleep Schedule")
        create.geometry("700x500")
        create.resizable(0, 0)
        create.mainloop()

    def about_popbox(self):
        about_input = "SETPy is an application that tracks and evaluate your sleeping routine.\
            \nIt will help you to track your sleeping hours and evaluate it if they are healthy or not.\
            \n Windows 10\
            \n Copyright 2022 Final Project 5"
        messagebox.showinfo("SETPy About", about_input)


LogInWindow()
