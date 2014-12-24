#Joey Smith and Minerva Chen
#12/17/14

from tkinter import *
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
		
		l = Label(self.top, text="Enter New Foods")
		l.grid(row=0, column=0, pady=15)
		
		l = Label(self.top, text="Nutrition Facts")
		l.grid(row=1, column=0)
		
		l = Label(self.top, text="Serving Size")
		l.grid(row=2, column=0)
		e = Entry(self.top)
		e.grid(row=2, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=2, column=2)
		
		l = Label(self.top, text="Amount Per Serving")
		l.grid(row=3, column=0)
		
		l = Label(self.top, text="Energy")
		l.grid(row=4, column=0)
		e = Entry(self.top)
		e.grid(row=4, column=1)
		en_unit = StringVar(self.top)
		en_unit.set("calories")
		drop = OptionMenu(self.top, en_unit, "calories", "kiloJoules")
		drop.grid(row=4, column=2)
		
		l = Label(self.top, text="Total Fat")
		l.grid(row=5, column=0)
		e = Entry(self.top)
		e.grid(row=5, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=5, column=2)
		
		l = Label(self.top, text="Saturated Fat")
		l.grid(row=6, column=0)
		e = Entry(self.top)
		e.grid(row=6, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=6, column=2)
		
		l = Label(self.top, text="Trans Fat")
		l.grid(row=7, column=0)
		e = Entry(self.top)
		e.grid(row=7, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=7, column=2)
		
		l = Label(self.top, text="Polyunsaturated Fat")
		l.grid(row=8, column=0)
		e = Entry(self.top)
		e.grid(row=8, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=8, column=2)
		
		l = Label(self.top, text="Cholesterol")
		l.grid(row=9, column=0)
		e = Entry(self.top)
		e.grid(row=9, column=1)
		l = Label(self.top, text="milligrams")
		l.grid(row=9, column=2)
		
		l = Label(self.top, text="Sodium")
		l.grid(row=10, column=0)
		e = Entry(self.top)
		e.grid(row=10, column=1)
		l = Label(self.top, text="milligrams")
		l.grid(row=10, column=2)
		
		l = Label(self.top, text="Total Carbohydrate")
		l.grid(row=11, column=0)
		e = Entry(self.top)
		e.grid(row=11, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=11, column=2)
		
		l = Label(self.top, text="Dietary Fiber")
		l.grid(row=12, column=0)
		e = Entry(self.top)
		e.grid(row=12, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=12, column=2)
		
		l = Label(self.top, text="Sugars")
		l.grid(row=13, column=0)
		e = Entry(self.top)
		e.grid(row=13, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=13, column=2)
		
		l = Label(self.top, text="Protein")
		l.grid(row=14, column=0)
		e = Entry(self.top)
		e.grid(row=14, column=1)
		l = Label(self.top, text="grams")
		l.grid(row=14, column=2)
		
		l = Label(self.top, text="Vitamin A")
		l.grid(row=15, column=0)
		e = Entry(self.top)
		e.grid(row=15, column=1)
		l = Label(self.top, text="%")
		l.grid(row=15, column=2)
		
		l = Label(self.top, text="Vitamin C")
		l.grid(row=15, column=3)
		e = Entry(self.top)
		e.grid(row=15, column=4)
		l = Label(self.top, text="%")
		l.grid(row=15, column=5)
		
		l = Label(self.top, text="Calcium")
		l.grid(row=16, column=0)
		e = Entry(self.top)
		e.grid(row=16, column=1)
		l = Label(self.top, text="%")
		l.grid(row=16, column=2)
		
		l = Label(self.top, text="Iron")
		l.grid(row=16, column=3)
		e = Entry(self.top)
		e.grid(row=16, column=4)
		l = Label(self.top, text="%")
		l.grid(row=16, column=5)
	
	#sets up the daily food tab
	def daily_food(self):
		self.current_tab = DAILYFOOD
		self.reset_top()
		print("daily_food")
	
	def daily_ex(self):
		self.current_tab = DAILYEX
		self.reset_top()
		print("daily_ex")
		
	
if __name__ == "__main__":
	t = TopLevel()
	t.run()