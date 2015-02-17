#Joey Smith and Minerva Chen
#12/17/14

#USE LAMBDAS TO BIND TO FUNCTIONS THAT TAKE ARGUMENTS!!

from tkinter import *
import tkinter.messagebox
import sus_sql as sql

NEWFOOD = 'NewFood'
DAILYFOOD = 'DailyFood'
DAILYEX = 'DailyEx'

# a top level class used to keep things organized
class TopLevel:
	
	def __init__(self):
		self.root = Tk()
		#sets size of window to 800px by 800px
		self.root.geometry("800x800")
		#sets the title bar text
		self.root.wm_title("Sustenance")
		
		# start in the current food tab
		self.current_tab = 'NewFood'
		
		# set up a dict of the different tabs
		self.tab_dict = {NEWFOOD : self.new_food, DAILYFOOD : self.daily_food, DAILYEX : self.daily_ex}
		
		# place these two lines before any other method calls from __init__
		self.top = Frame(self.root)
		self.top.pack(ipadx=10, ipady=10)
		
		self.menu_bar()
	
	# runs the gui code
	def run(self):
		self.root.mainloop()
	
	# creates the menu bar at the top
	def menu_bar(self):
		#menu bar must be a subwidget of root
		menubar = Menu(self.root)
		menubar.add_command(label="New Foods", command=self.new_food)
		menubar.add_command(label="Daily Food", command=self.daily_food)
		menubar.add_command(label="Daily Exercise", command=self.daily_ex)
		
		self.root.config(menu=menubar)
	
	# DUMMY METHOD
	def hello(self):
		print("hello")	
	
	# DUMMY METHOD
	def fellow(self):
		print("fellow")
	
	# resets all the widgets on the page by deleting the top level frame and recreating it
	def reset_top(self):
		self.top.destroy()
		self.top = Frame(self.root)
		self.top.pack(ipadx=10, ipady=10)
	
	# sets up the new food tab
	# MADE TO LOOK LIKE NUTRITION FACTS?
	# MIGHT BE POSSIBLE TO CREATE A FRAME WITHIN SELF.TOP AND THEN USE THE 'PLACE' TKINTER THING TO PLACE ALL THE STUFF IN THE RIGHT AREA
	# FIND A WAY TO MOVE TO NEXT THING BY PRESSING 'ENTER'
	def new_food(self):
		self.current_tab = NEWFOOD
		self.reset_top()
		print("new_food")
		
		self.nutr_lst = []
		
		l = Label(self.top, text="Enter New Foods")
		l.grid(row=0, column=0, pady=15)
		
		l = Label(self.top, text="Name of Food *")
		l.grid(row=1, column=0, pady=5)
		e = Entry(self.top)
		e.grid(row=1, column=1)
		self.nutr_lst.append(e)
		
		l = Label(self.top, text="Nutrition Facts")
		l.grid(row=2, column=0)
		
		l = Label(self.top, text="Serving Size*")
		l.grid(row=3, column=0)
		e = Entry(self.top)
		e.grid(row=3, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=3, column=2)
		self.nutr_lst.append(e)
		
		l = Label(self.top, text="Amount Per Serving")
		l.grid(row=4, column=0)
		
		nutrition = ["Energy*", "Total Fat", "Saturated Fat", "Trans Fat", "Polyunsaturated Fat", "Monounsaturated Fat", "Cholesterol", "Sodium", "Total Carbohydrate", "Dietary Fiber", "Sugars", "Protein"]
		
		for i in range(len(nutrition)):
			l = Label(self.top, text=nutrition[i])
			l.grid(row=i+5, column=0)
			e = Entry(self.top)
			e.grid(row=i+5, column=1)
			if nutrition[i] == "Sodium" or nutrition[i] == "Cholesterol":
				l = Label(self.top, text="milligrams")
			else:
				l = Label(self.top, text="grams")
			l.grid(row=i+5, column=2)
			self.nutr_lst.append(e)
		
		en_unit = StringVar(self.top)
		en_unit.set("calories")
		drop = OptionMenu(self.top, en_unit, "calories", "kiloJoules")
		drop.grid(row=5, column=2)
		
		l = Label(self.top, text="Vitamin A")
		l.grid(row=18, column=0)
		e = Entry(self.top)
		e.grid(row=18, column=1)
		l = Label(self.top, text="%")
		l.grid(row=18, column=2)
		self.nutr_lst.append(e)
		 
		l = Label(self.top, text="Vitamin C")
		l.grid(row=18, column=3)
		e = Entry(self.top)
		e.grid(row=18, column=4)
		l = Label(self.top, text="%")
		l.grid(row=18, column=5)
		self.nutr_lst.append(e)
		
		l = Label(self.top, text="Calcium")
		l.grid(row=19, column=0)
		e = Entry(self.top)
		e.grid(row=19, column=1)
		l = Label(self.top, text="%")
		l.grid(row=19, column=2)
		self.nutr_lst.append(e)
		
		l = Label(self.top, text="Iron")
		l.grid(row=19, column=3)
		e = Entry(self.top)
		e.grid(row=19, column=4)
		l = Label(self.top, text="%")
		l.grid(row=19, column=5)
		self.nutr_lst.append(e)
		
		l = Label(self.top, text="* Required field")
		l.grid(row=21, column=1)
		
		for i in range(0, len(self.nutr_lst) - 1):
			self.nutr_lst[i].bind("<Return>", lambda x: self.nutr_lst[i + 1].focus_set())
		
		# the button sends the command to insert the info into the food sql table
		b = Button(self.top, text="Enter", command= lambda: self.test_and_enter(self.nutr_lst, en_unit))
		b.grid(row=20, column=3)
	
	# returns a list of the strings inside each of the members of a list of Entry widgets
	# also converts kiloJoules to food calories if necessary
	def get_new_food_entries(self, lst, unit):
		#SHOULD BE PYTHON 2.X COMPATIBLE, BUT DOUBLE CHECK
		# gets the info from the
		print(lst)
		info = list(map(lambda x: x.get(), lst))
		print(info)
		
		# converts kiloJoule energy to food calories
		if unit.get() == "kiloJoules" and info[2] != '':
			energy = float(info[2])
			energy = 0.239 * energy
			info[2] = str(energy)
		return info
		
	# tests if the required fields are filled and enters the info into the database if so
	def test_and_enter(self, info, en_unit):
		info = self.get_new_food_entries(self.nutr_lst, en_unit)
		print(info)
		if info[0] == '' or info[1] == '' or info[2] == '':
			tkinter.messagebox.showwarning('Retry Entry', 'You must include "Name of Food", "Serving Size", and "Energy"')
			# prevents entry into database
			return
		else:
			# clears the text in the entry
			map(lambda x: x.delete(0, END), self.nutr_lst)
			sql.insert_new_food(info)
	
	#sets up the daily food tab
	def daily_food(self):
		self.current_tab = DAILYFOOD
		self.reset_top()
		print("daily_food")
	
	# sets up the daily exercise tab
	def daily_ex(self):
		self.current_tab = DAILYEX
		self.reset_top()
		print("daily_ex")
		
	
if __name__ == "__main__":
	t = TopLevel()
	t.run()
	sql.save_and_close() # required to make changes permanent