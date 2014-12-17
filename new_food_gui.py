#Joey Smith and Minerva Chen
#12/16/14

#add Joules in for those crazy foreigners hahaha

#CHANGE TO Tkinter FOR PYTHON 2
from tkinter import *
import new_food_sql as sql

class NewFood:
	
	def __init__(self, master):
		frame = Frame(master)
		frame.pack(padx=30, ipadx=10, ipady=10)
		self.new_food_labels(frame)
		
		self.entries(frame)
		
		e = Button(frame, text="Enter", command=self.insert)
		
		e.grid(row=2, column=5, padx=30)
		
	def insert(self):
		sql.insert_food(6, "grams", 12, 23, "daily %")
		
		
	#sets up the labels row
	def new_food_labels(self, frame):
		l = Label(frame, text="Enter New Foods")
		l.grid(row=0, column=2, pady=15)
		
		serv = Label(frame, text="serving size")
		serv.grid(row=1, column=0)
		
		cal = Label(frame, text="calories")
		cal.grid(row=1, column=2)
		
		vitA = Label(frame, text="vitamin A")
		vitA.grid(row=1, column=3)
	
	# sets up the entries row
	def entries(self, frame):
		size = Entry(frame)
		size.grid(row=2, column=0)
		
		size_unit = StringVar(frame)
		size_unit.set("grams")
		
		drop = OptionMenu(frame, size_unit, "grams", "ounces")
		drop.grid(row=2, column=1)
		
		cal = Entry(frame)
		cal.grid(row=2, column=2, padx=30)
		
		
		vitA = Entry(frame)
		vitA.grid(row=2, column=3)
		
		vit_unit = StringVar(frame)
		vit_unit.set("daily %")
		
		drop = OptionMenu(frame, vit_unit, "daily %", "milligrams")
		drop.grid(row=2, column=4)
		
		

root = Tk()

new_food = NewFood(root)


mainloop()
root.mainloop()
#root.destroy() ONLY USE IF YOU MAKE YOUR OWN EXIT HANDLER!!