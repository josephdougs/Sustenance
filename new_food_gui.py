#Joey Smith and Minerva Chen
#12/16/14
#THIST IS THE PYTHON 2 VERISON.  CHANGE TO PYTHON 3 LATER??

from Tkinter import *

class NewFood:
    
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        
        self.labels(frame)
        
        self.entries(frame)
        
        e = Button(frame, text="Enter")
        e.grid(row=2, column=3)

    def labels(frame):
        l = Label(frame, text="Enter New Foods")
        l.grid(row=0, column=1)
        
        serv = Label(frame, text="serving size (grams)")
        serv.grid(row=1, column=0)
        
        cal = Label(frame, text="calories")
        cal.grid(row=1, column=1)
        
        vitA = Label(frame, text="vitamin A (Daily %)")
        vitA.grid(row=1, column=2)
    
    def entries(frame):
        for i in range(3):
            e = Entry(frame)
            e.grid(row=2, column=i)

root = Tk()

new_food = NewFood(root)


mainloop()
root.mainloop()
root.destroy() #is this good?  On Mac at least it throws an error if
# i close with the x button b/c this can't be destroyed, since the button
#destroyed it
