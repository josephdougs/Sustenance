#Joey Smith and Minerva Chen
#12/16/14

#CHANGE TO Tkinter FOR PYTHON 2
from tkinter import *

class NewFood:
	
	def __init__(self, master):
		frame = Frame(master)
		frame.pack(padx=30, ipadx=10, ipady=10)
		self.new_food_labels(frame)
		
		self.entries(frame)
		
		e = Button(frame, text="Enter")
		e.grid(row=2, column=5)
		
	#sets up the labels row
	def new_food_labels(self, frame):
		l = Label(frame, text="Enter New Foods")
		l.grid(row=0, column=2, pady=15)
		
		serv = Label(frame, text="serving size")
		serv.grid(row=1, column=0)
		
		cal = Label(frame, text="calories")
		cal.grid(row=1, column=2)
		
		vitA = Label(frame, text="vitamin A")
		vitA.grid(row=1, column=4)
	
	# sets up the entries row
	def entries(self, frame):
		size = Entry(frame)
		size.grid(row=2, column=0)
		
		size_unit = StringVar(frame)
		size_unit.set("grams")
		
		drop = OptionMenu(frame, size_unit, "grams", "ounces")
		drop.grid(row=2, column=1, padx=10)
		
		cal = Entry(frame)
		cal.grid(row=2, column=2, padx=10)
		
		unit2 = StringVar(frame)
		unit2.set("Daily %")
		
		drop = OptionMenu(frame, unit2, "Daily %", "milligrams")
		drop.grid(row=2, column=3, padx=10)
		
		e = Entry(frame)
		e.grid(row=2, column=4, padx=10)
		
		

root = Tk()

new_food = NewFood(root)


mainloop()
root.mainloop()
root.destroy() #is this good?  On Mac at least it throws an error if
# i close with the x button b/c this can't be destroyed, since the button
#destroyed it
#UPDATE: IT DOES THIS ON WINDOWS TOO!!