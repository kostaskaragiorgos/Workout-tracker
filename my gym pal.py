from tkinter import *
from tkinter import messagebox as msg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import os 
import csv
import datetime

class MyGymPal():
    def __init__(self,master):
        self.master = master
        self.master.title("My Gym Pal")
        self.master.geometry("250x250")
        self.master.resizable(False,False)
        nowyear = datetime.date.today().year
        
        if os.path.exists(str(nowyear)) == False:
            os.mkdir(str(nowyear))
            os.chdir(str(nowyear))
        else:
            os.chdir(str(nowyear))
        
        self.nowmonth = datetime.date.today().month
        if os.path.exists('My Gyn Pal'+str(self.nowmonth)+'.csv') == False:
            with open('My Gyn Pal'+str(self.nowmonth)+'.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['Day','Name of the exercise','No of sets','No of reps','Kg'])
                f.close()
                
        self.exname = Label(self.master,
                               text = "Enter the name of the exercise")
        self.exname.pack()
        
        self.textname = Text(self.master,height = 1 )
        self.textname.pack()
        
        self.setsleb = Label(self.master,text="Sets")
        self.setsleb.pack()
        setslist = list(range(1,21))
        self.varnumset = StringVar(master)
        self.varnumset.set(setslist[0])
        self.popupsetmenu = OptionMenu(self.master,self.varnumset,*setslist)
        self.popupsetmenu.pack()
        
        self.reps = Label(self.master,text="Reps:")
        self.reps.pack()
        repslist = list(range(1,41))
        self.varnumreps = StringVar(master)
        self.varnumreps.set(repslist[0])
        self.popuprepsmenu = OptionMenu(self.master,self.varnumreps,*repslist)
        self.popuprepsmenu.pack()
        
        self.kgleb = Label(self.master,text="Kg:")
        self.kgleb.pack()
        self.kgslider = Scale(self.master,from_=0 , to = 300,orient= HORIZONTAL)
        self.kgslider.pack()
def main():
    root=Tk()
    mgp = MyGymPal(root)
    root.mainloop()
    
if __name__=='__main__':
    main()