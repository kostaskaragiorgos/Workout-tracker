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
    listoffiles = os.listdir()
    msg.showinfo("Montly Workout", "Day(s) of workout: "+str(len(listoffiles)))  
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Enter the name of the exercise, the number of sets,reps and the kg amount and press the submit button to save the data ")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "My Gym Pal\nVersion 1.0")
class MyGymPal():
    """ My gym pal class """
    def __init__(self, master):
        self.master = master
        self.master.title("My Gym Pal")
        self.master.geometry("270x290")
        self.master.resizable(False, False)
        nowyear = datetime.date.today().year
        nowmonth = datetime.date.today().month
        if not os.path.exists(str(nowyear)):
            os.mkdir(str(nowyear))
            os.chdir(str(nowyear))
        else:
            os.chdir(str(nowyear))
        if not os.path.exists(str(nowmonth)):
            os.mkdir(str(nowmonth))
            os.chdir(str(nowmonth))
        else:
            os.chdir(str(nowmonth))
        self.nowday = datetime.date.today().day
        #menu
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Submit Exercise", accelerator='Alt+O',
                                   command=self.submitb)
        self.file_menu.add_command(label="Reset", accelerator='Alt+R', command=self.reset)
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4',
                                   command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.menu, tearoff=0)
        self.edit_menu.add_command(label="Clear Name", accelerator='Ctrl + S',
                                   command=self.clearname)
        self.menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Today's Workout", accelerator='Alt+W', command=self.towork)
        self.show_menu.add_command(label="Total workouts this month", accelerator='Alt+T', command=totwork)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.master.bind('<Alt-o>', lambda event: self.submitb())
        self.master.bind('<Alt-t>', lambda event: totwork())
        self.master.bind('<Alt-w>', lambda event: self.towork())
        self.master.bind('<Alt-r>', lambda event: self.reset())
        self.master.bind('<Control-s>', lambda event: self.clearname())
        self.exname = Label(self.master,
                            text="Enter the name of the exercise")
        self.exname.pack()
        self.textname = Text(self.master, height=1)
        self.textname.pack()
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
    def reset(self):
        """ reset button function """
        self.varnumreps.set(self.repslist[0])
        self.varnumset.set(self.setslist[0])
        self.kgslider.set(0)
        self.textname.delete(1.0, END)
    def clearname(self):
        """ clear name text field """
        self.textname.delete(1.0, END)
    def towork(self):
        """ workout summary of the day """
        if not os.path.exists('My Gyn Pal'+str(self.nowday)+'.csv'):
            msg.showerror("No Exercises", "No exercises saved")
        else:
            df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
            df = df.drop_duplicates(keep="first")
            df = df.replace(r'\r\n','',regex=True)
            msg.showinfo("Today's Workout", str(df))
    def submitb(self):
        """ submit button function """
        if self.textname.count(1.0, END) == (1, ):
            msg.showerror("Name Error", "Enter the name of the  exercise")
        else:
            if not os.path.exists('My Gyn Pal'+str(self.nowday)+'.csv'):
                with open('My Gyn Pal'+str(self.nowday)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['Name of the exercise', 'No of sets', 'No of reps', 'Kg'])
                    thewriter.writerow([str(self.textname.get(1.0, END)), str(self.varnumset.get()), str(self.varnumreps.get()), str(self.kgslider.get())])
            else:
                with open('My Gyn Pal'+str(self.nowday)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(self.textname.get(1.0, END)), str(self.varnumset.get()), str(self.varnumreps.get()), str(self.kgslider.get())])
            msg.showinfo("Your exersice", "Name of the exercise:"+str(self.textname.get(1.0, END))+"Reps:"+str(self.varnumreps.get())+"Sets:"+str(self.varnumset.get())+"Kg:"+str(self.kgslider.get()))
            self.varnumreps.set(self.repslist[0])
            self.varnumset.set(self.setslist[0])
            self.kgslider.set(0)
            self.textname.delete(1.0, END)
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