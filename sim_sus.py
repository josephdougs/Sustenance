#Joey Smith and Minerva Chen
#12/17/14

#USE LAMBDAS TO BIND TO FUNCTIONS THAT TAKE ARGUMENTS!!

"""On the organization of this code:
	
	You are currently looking at the main module for this project, so if you are trying to
	understand this code, you are looking in the right place.
	
	The code is currently divided into two modules.  This one, 'sim_sus.py', is the main 
	module that handles all GUI stuff and also some data conversions.
	The other module, 'sus_sql.py' handles interactions	with the sqlite3 database.
	
	This module is organized as a class (TopLevel).  The class '__init__' method of the class
	sets up the basics for the GUI, and the 'run' method runs the tkinter mainloop, which
	is what actually starts running the tkinter GUI.
	
	This program has several sections, each with a different functionality.  The user may select
	these sections using the menubar at the top of the GUI.  The sections are currently 'New Foods',
	'Daily Foods', and 'Daily Exercise'.  Not all of these are currently finished, and more may be
	added later.
	
	'New Foods' is where the user enters nutritional information about foods that they have eaten
	for the first time.  The foods must have a UNIQUE name.  This is important as it is how the
	program identifies them later.
	
	'Daily Foods' is where the user enters what foods and how much of each they have eaten that
	day.
	
	'Daily Exercise' is where the user enters how and how much they exercised that day.
	
	Other methods are typically helpers for each of theses sections.


"""


'''
REMINDER OF ORDER
(name text, serv_size real, cals real, tot_fat real, s_fat real, tr_fat real,
			 p_fat real, m_fat real, cholest real, sodium real, tot_carb real, fiber real, 
			 sugars real, protein real, vit_a real, vit_c real, calcium real, iron real)'''


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
		
		
		# set up a dict of the different tabs
		self.tab_dict = {NEWFOOD : self.new_food, DAILYFOOD : self.daily_food, DAILYEX : self.daily_ex}
		
		# place these two lines before any other method calls from __init__
		self.top = Frame(self.root)
		self.top.pack(ipadx=10, ipady=10)
		
		self.menu_bar()
		
		# start in the new food tab
		self.new_food()
	
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
		s_unit = StringVar(self.top)
		s_unit.set("grams")
		drop = OptionMenu(self.top, s_unit, "grams", "ounces")
		drop.grid(row=3, column=2)
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
		
		# IGNORE THIS FOR NOW, GET BACK TO IT LATER;  IS NOT ESSENTIAL
		'''for i in range(0, len(self.nutr_lst) - 1):
			self.nutr_lst[i].bind("<Return>", lambda x: self.nutr_lst[i + 1].focus_set())'''
		
		# the button sends the command to insert the info into the food sql table
		b = Button(self.top, text="Enter", command= lambda: self.test_and_enter(self.nutr_lst, s_unit.get(), en_unit.get()))
		b.grid(row=20, column=2)
	
	# tests if the required fields are filled and enters the info into the database if so
	def test_and_enter(self, info, s_unit, en_unit):
		info = self.get_new_food_entries(info, s_unit, en_unit)
		
		test = sql.get_food(info[0])		
		if test != None:
			text = 'Retry Entry', 'Food "' + info[0] + '" is already present in the database.\n'
			text += 'Its information is:\n'
			text += 'Serving size: ' + test[1] + 'Energy: ' + test[2] + '(in calories)'
			answer = tkinter.messagebox.askyesno(text)
			
		print(info)
		if info[0] == '' or info[1] == '' or info[2] == '':
			tkinter.messagebox.showwarning('Retry Entry', 'You must include "Name of Food", "Serving Size", and "Energy"')
			# prevents entry into database
			return
		else:
			# clears the text in the entry
			map(lambda x: x.delete(0, END), self.nutr_lst)
			sql.insert_new_food(info)
	
	# returns a list of the strings inside each of the members of a list of Entry widgets
	# also converts units if necessary
	def get_new_food_entries(self, lst, s_unit, en_unit):
		#SHOULD BE PYTHON 2.X COMPATIBLE, BUT DOUBLE CHECK
		# gets the info from the
		print(lst)
		info = list(map(lambda x: x.get(), lst))
		print(info)
		
		if s_unit == "ounces" and info[1] != '':
			mass = float(info[1])
			mass = 28.3495 * mass
			info[1] = str(mass)
		
		# converts kiloJoule energy to food calories
		if en_unit == "kiloJoules" and info[2] != '':
			energy = float(info[2])
			energy = 0.239 * energy
			info[2] = str(energy)
		
		return info
	
	#sets up the daily food tab
	def daily_food(self):
		
		self.current_tab = DAILYFOOD
		self.reset_top()
		print("daily_food")
		
		l = Label(self.top, text="Enter Today's Foods")
		l.grid(row=0, column=0, pady=15)
		
		l = Label(self.top, text="Name of Food")
		l.grid(row=1, column=0, pady=5)
		name_e = Entry(self.top)
		name_e.grid(row=1, column=1)
		
		l = Label(self.top, text="Amount")
		l.grid(row=1, column=3, pady=5)
		am_e = Entry(self.top)
		am_e.grid(row=1, column=4)
		a_unit = StringVar(self.top)
		a_unit.set("grams")
		drop = OptionMenu(self.top, a_unit, "grams", "ounces", "servings")
		drop.grid(row=1, column=5, padx=15)
		
		lb = Listbox(self.top, height=35, width=100)
		lb.grid(row=2, column=1, columnspan=5, padx=15)
		
		add = Button(self.top, text="Add", command= lambda: self.add_list_food(name_e.get(), am_e.get(), a_unit.get(), lb))
		add.grid(row=1, column=6)
	
	# checks that the food exists and if it does, adds it to the listbox
	def add_list_food(self, name, amount, unit, lb):
		# DO A TEST TO SEE IF ANY ARE EMPTY!!!
		if name == '' or amount == '':
			tkinter.messagebox.showwarning('Retry Entry', 'Please include both the name of the food and how much of it you ate.')
			return
		print(name)
		food = sql.get_food(name)
		if food == None:
			tkinter.messagebox.showwarning('Retry Entry', 'Food: "' + name + '''" does not appear to exist in the database.
Check the spelling or enter the food into the database using the
"New Foods" tab.''')
			return # MAKE SURE THIS DOES NOT HAVE TO RETURN ANYTHING
		
		food = list(food) # converts food from a tuple to a list
		
		# turns amount into a number of servings
		if unit == "grams":
			amount = food[1] / float(amount) #CHECK FOR DIVIDE BY ZERO?
		elif unit == "ounces": #CHECK THIS ONE
			amount = food[1] / (28.3495 * float(amount))
		else:
			amount = float(amount)
		
	
	# sets up the daily exercise tab
	def daily_ex(self):
		self.current_tab = DAILYEX
		self.reset_top()
		print("daily_ex")
		
	
if __name__ == "__main__":
	t = TopLevel()
	t.run()
	sql.save_and_close() # required to make changes permanent