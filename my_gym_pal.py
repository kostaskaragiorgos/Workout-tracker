"""
helps you tack your workouts
"""
from tkinter import Tk, Menu, Label, Text, Scale, Button, StringVar, OptionMenu
from tkinter import HORIZONTAL, END, messagebox as msg
import os
import csv
import datetime
import pandas as pd
def totwork():
    """ days of workout this month"""
    msg.showinfo("Montly Workout", "Day(s) of workout: "+str(len(os.listdir())))
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Enter the name of the exercise," +
                 "the number of sets,reps and the kg amount "+
                 "and press the submit button to save the data ")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "My Gym Pal\nVersion 1.0")
def checkfolder(folder):
    """ creates a folder and changes the current directory """
    if not os.path.exists(str(folder)):
        os.mkdir(str(folder))
    os.chdir(str(folder))
def createcsv(filename):
    """ creates the csv file to save the exercises"""
    if not os.path.exists(filename):
        with open(filename, 'a+') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['Name of the exercise', 'Difficulty', 'No of sets', 'No of reps', 'Kg'])

class MyGymPal():
    """ My gym pal class """
    def __init__(self, master):
        self.master = master
        self.master.title("My Gym Pal")
        self.master.geometry("280x340")
        self.master.resizable(False, False)
        nowyear = datetime.date.today().year
        nowmonth = datetime.date.today().month
        checkfolder(nowyear)
        checkfolder(nowmonth)
        self.nowday = datetime.date.today().day
        # file creation
        createcsv('My Gyn Pal'+str(self.nowday)+'.csv')
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Submit Exercise", accelerator='Alt+O',
                                   command=self.submitb)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4',
                                   command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.clearsubmenu = Menu(self.edit_menu, tearoff=0)
        self.clearsubmenu.add_command(label="Difficulty", accelerator="Alt-D")
        self.clearsubmenu.add_command(label="Sets", accelerator="Ctrl+T")
        self.clearsubmenu.add_command(label="Reps", accelerator="Ctrl+W")
        self.clearsubmenu.add_command(label="Kg", accelerator="Ctrl+R")
"""
        self.master.bind('<Control-s>', lambda event: self.reset(toclear=self.textname))
        self.master.bind('<Control-w>', lambda event: self.reset(toclear=self.varnumreps, textflag=False, text=self.repslist[0]))
        self.master.bind('<Control-r>', lambda event: self.reset(toclear=self.kgslider, textflag=False, text= 0))
        self.master.bind('<Control-t>', lambda event: self.reset(toclear=self.varnumset, textflag=False, textl= self.setslist[0]))
        self.master.bind('<Alt-d>', lambda event: self.reset(toclear=self.diffstring, textflag=False, text=self.difflist[0]))
"""

        self.edit_menu.add_cascade(label="Reset", menu=self.clearsubmenu, underline=0)
        self.edit_menu.add_command(label="Reset All", accelerator='Alt+R', command=self.reset)
        self.edit_menu.add_command(label="Clear Name", accelerator='Ctrl+S',
                                   command=lambda: self.reset(toclear=self.textname))
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.submenu = Menu(self.show_menu, tearoff=0)
        self.submenu.add_command(label="Easy", accelerator='Ctrl+D', command=self.showeasy)
        self.submenu.add_command(label="Hard", accelerator='Ctrl+O', command=self.showhard)
        self.submenu.add_command(label="Medium", accelerator='Ctrl+U', command=self.showmedium)
        self.submenu.add_command(label="Unable to do", accelerator='Ctrl+Y', command=self.showunabletodo)
        self.show_menu.add_cascade(label="Most used per Difficulty",
                                   menu=self.submenu, underline=0)
        self.show_menu.add_command(label="Today's Workout",
                                   accelerator='Alt+W', command=self.towork)
        self.show_menu.add_command(label="Total workouts this month",
                                   accelerator='Alt+T', command=totwork)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-d>', lambda event: self.showeasy())
        self.master.bind('<Control-o>', lambda event: self.showhard())
        self.master.bind('<Control-u>', lambda event: self.showmedium())
        self.master.bind('<Control-y>', lambda event: self.showunabletodo())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.submitb())
        self.master.bind('<Alt-t>', lambda event: totwork())
        self.master.bind('<Alt-w>', lambda event: self.towork())
        self.master.bind('<Alt-r>', lambda event: self.reset())
        self.master.bind('<Control-s>', lambda event: self.reset(toclear=self.textname))
        self.master.bind('<Control-w>', lambda event: self.reset(toclear=self.varnumreps, textflag=False, text=self.repslist[0]))
        self.master.bind('<Control-r>', lambda event: self.reset(toclear=self.kgslider, textflag=False, text= 0))
        self.master.bind('<Control-t>', lambda event: self.reset(toclear=self.varnumset, textflag=False, textl= self.setslist[0]))
        self.master.bind('<Alt-d>', lambda event: self.reset(toclear=self.diffstring, textflag=False, text=self.difflist[0]))


        self.exname = Label(self.master,
                            text="Enter the name of the exercise")
        self.exname.pack()
        self.textname = Text(self.master, height=1)
        self.textname.pack()
        self.diff = Label(self.master, text="Difficulty")
        self.diff.pack()
        self.difflist = ["Easy", "Medium", "Hard", "Unable to do"]
        self.diffstring = StringVar(master)
        self.diffstring.set(self.difflist[0])
        self.diffpopup = OptionMenu(self.master, self.diffstring, *self.difflist)
        self.diffpopup.pack()
        self.setsleb = Label(self.master, text="Sets")
        self.setsleb.pack()
        self.setslist = list(range(1, 21))
        self.varnumset = StringVar(master)
        self.varnumset.set(self.setslist[0])
        self.popupsetmenu = OptionMenu(self.master, self.varnumset, *self.setslist)
        self.popupsetmenu.pack()
        self.reps = Label(self.master, text="Reps")
        self.reps.pack()
        self.repslist = list(range(1, 41))
        self.varnumreps = StringVar(master)
        self.varnumreps.set(self.repslist[0])
        self.popuprepsmenu = OptionMenu(self.master, self.varnumreps, *self.repslist)
        self.popuprepsmenu.pack()
        self.kgleb = Label(self.master, text="Kg")
        self.kgleb.pack()
        self.kgslider = Scale(self.master, from_=0, to=300, tickinterval=100, orient=HORIZONTAL)
        self.kgslider.pack()
        self.subb = Button(self.master, text="Submit", command=self.submitb)
        self.subb.pack()
        self.resetb = Button(self.master, text="Reset", command=self.reset)
        self.resetb.pack()
    
    def showhard(self):
        """ shows the hard to do exercises"""
        df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
        df.drop_duplicates(keep="first", inplace=True)
        df.replace(r'\r\n', '', regex=True, inplace=True)
        if df.shape == (0,5):
            msg.showerror("ERROR" , "NO WORKOUTS")
        else:
            msg.showinfo("Hard",str([df[df['Difficulty']=="Hard"]['Name of the exercise']]))

    def showunabletodo(self):
        """ shows the unable  to do exercises"""
        df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
        df.drop_duplicates(keep="first", inplace=True)
        df.replace(r'\r\n', '', regex=True, inplace=True)
        if df.shape == (0,5):
            msg.showerror("ERROR" , "NO WORKOUTS")
        else:
            msg.showinfo("Unable to do",str([df[df['Difficulty']=="Unable to do"]['Name of the exercise']]))
            
    
    def showmedium(self):
        """ shows the medium to do exercises"""
        df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
        df.drop_duplicates(keep="first", inplace=True)
        df.replace(r'\r\n', '', regex=True, inplace=True)
        if df.shape == (0,5):
            msg.showerror("ERROR" , "NO WORKOUTS")
        else:
            msg.showinfo("Medium",str([df[df['Difficulty']=="Medium"]['Name of the exercise']]))

    def showeasy(self):
        """ shows the easy to do exercises"""
        df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
        df.drop_duplicates(keep="first", inplace=True)
        df.replace(r'\r\n', '', regex=True, inplace=True)
        if df.shape == (0,5):
            msg.showerror("ERROR" , "NO WORKOUTS")
        else:
            msg.showinfo("Easy",str([df[df['Difficulty']=="Easy"]['Name of the exercise']]))

    def reset(self, toclear=None, textflag=True, text=""):
        """ reset button function """
        if toclear is None:
            self.varnumreps.set(self.repslist[0])
            self.varnumset.set(self.setslist[0])
            self.kgslider.set(0)
            self.textname.delete(1.0, END)
        elif textflag:
            toclear.delete(1.0,END)
        else:
            toclear.set(text)


    def towork(self):
        """ workout summary of the day """
        df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
        df.drop_duplicates(keep="first", inplace=True)
        df.replace(r'\r\n', '', regex=True, inplace=True)
        if df.shape == (0,5):
            msg.showerror("ERROR" , "NO WORKOUTS")
        else:    
            msg.showinfo("Today's Workout", str(df))
    def submitb(self):
        """ submit button function """
        if self.textname.count(1.0, END) == (1, ):
            msg.showerror("Name Error", "Enter the name of the  exercise")
        else:
            
            with open('My Gyn Pal'+str(self.nowday)+'.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([str(self.textname.get(1.0, END)),
                                    str(self.diffstring.get()),
                                    str(self.varnumset.get()),
                                    str(self.varnumreps.get()),
                                    str(self.kgslider.get())])
            msg.showinfo("Your exersice", "Name of the exercise:"
                         +str(self.textname.get(1.0, END))+" Difficulty: "+str(self.diffstring.get())+"Reps:"
                         +str(self.varnumreps.get())+"Sets:"
                         +str(self.varnumset.get())+"Kg:"+
                         str(self.kgslider.get()))
            self.reset()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function"""
    root = Tk()
    MyGymPal(root)
    root.mainloop()
if __name__ == '__main__':
    main()
