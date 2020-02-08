from tkinter import *
from tkinter import messagebox as msg

import os 
import csv
import datetime
import pandas as pd


class MyGymPal():
    def __init__(self,master):
        self.master = master
        self.master.title("My Gym Pal")
        self.master.geometry("270x270")
        self.master.resizable(False,False)
        
        nowyear = datetime.date.today().year
        
        nowmonth = datetime.date.today().month
        
        if os.path.exists(str(nowyear)) == False:
            os.mkdir(str(nowyear))
            os.chdir(str(nowyear))
        else:
            os.chdir(str(nowyear))
        
        if os.path.exists(str(nowmonth)) == False:
            os.mkdir(str(nowmonth))
            os.chdir(str(nowmonth))
        else:
            os.chdir(str(nowmonth))
            
        self.nowday = datetime.date.today().day

        #menu
            
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label = "Submit Exercise", accelerator = 'Alt+O',command = self.submitb)
        self.file_menu.add_command(label="Exit",accelerator= 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)

        self.edit_menu = Menu(self.menu,tearoff = 0 )
        self.edit_menu.add_command(label = "Clear Name",command = self.clearname)
        self.menu.add_cascade(label = "Edit",menu = self.edit_menu)
        
        self.show_menu = Menu(self.menu,tearoff = 0)
        self.show_menu.add_command(label = "Today's Workout",accelerator = 'Alt+W',command = self.towork)
        self.show_menu.add_command(label = "Total workouts this month",accelerator = 'Alt+T',command =self.totwork)
        self.menu.add_cascade(label = "Show",menu = self.show_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator= 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)
        
        self.master.config(menu=self.menu)
        
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        self.master.bind('<Alt-o>',lambda event:self.submitb())
        self.master.bind('<Alt-t>',lambda event:self.totwork())
        self.master.bind('<Alt-w>',lambda event:self.towork())
        
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
        
        self.reps = Label(self.master,text="Reps")
        self.reps.pack()
        
        self.repslist = list(range(1,41))
        self.varnumreps = StringVar(master)
        self.varnumreps.set(self.repslist[0])
        self.popuprepsmenu = OptionMenu(self.master,self.varnumreps,*self.repslist)
        self.popuprepsmenu.pack()
        
        self.kgleb = Label(self.master,text="Kg")
        self.kgleb.pack()
        
        self.kgslider = Scale(self.master,from_=0 , to = 300,tickinterval = 100 ,orient= HORIZONTAL)
        self.kgslider.pack()
        
        self.subb = Button(self.master,text = "Submit",command = self.submitb)
        self.subb.pack()
        
        #self.resetb = Button(self.master,text = "Reset")
        #self.resetb.pack() TODO
    
    def clearname(self):
        self.textname.delete(1.0,END)

    
    def towork(self):
        if os.path.exists('My Gyn Pal'+str(self.nowday)+'.csv') == False:
            msg.showerror("No Exercises","No exercises saved")
        else:
            df = pd.read_csv('My Gyn Pal'+str(self.nowday)+'.csv')
            msg.showinfo("Today's Workout",str(df))
        
        
    def submitb(self):
        if self.textname.count(1.0,END) == (1,):
            msg.showerror("Name Error", "Enter the name of the  exercise")
        else:
            if os.path.exists('My Gyn Pal'+str(self.nowday)+'.csv') == False:
                with open('My Gyn Pal'+str(self.nowday)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow(['Name of the exercise','No of sets','No of reps','Kg'])
                    f.close()
                
            else:
                with open('My Gyn Pal'+str(self.nowday)+'.csv', 'a+') as f:
                    thewriter = csv.writer(f)
                    thewriter.writerow([str(self.textname.get(1.0,END)),str(self.varnumset.get()),str(self.varnumreps.get()),str(self.kgslider.get())])
                    f.close()
            
            msg.showinfo("Your exersice","Name of the exercise:"+str(self.textname.get(1.0,END))+"Reps:"+str(self.varnumreps.get())+"Sets:"+str(self.varnumset.get())+"Kg:"+str(self.kgslider.get()))
            self.textname.delete(1.0,END)
            
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    
    def helpmenu(self):
        msg.showinfo("Help","Enter the name of the exercise, the number of sets,reps and the kg amount and press the submit button to save the data ")
        
    def aboutmenu(self):
        msg.showinfo("About", "My Gym Pal\nVersion 1.0")
    
    def totwork(self):
        listoffiles = os.listdir()
        msg.showinfo("Montly Workout","Day(s) of workout: "+str(len(listoffiles)))
        
        
def main():
    root=Tk()
    mgp = MyGymPal(root)
    root.mainloop()
    
if __name__=='__main__':
    main()