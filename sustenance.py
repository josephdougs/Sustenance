#Joey Smith and Minerva Chen
#12/17/14

from tkinter import *

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
		self.tab_dict = {NEWFOOD : self.new_food, DAILYINFO : self.daily_food, DAILYEX : self.daily_ex}
		
		# place these two lines before any other method calls from __init__
		self.top = Frame(self.root)
		self.top.pack(ipadx=10, ipady=10)
		
		self.is_quick = False
		self.menu_bar()
		
		
		
		#self.quick_new_food()
	
	
	# runs the gui code
	def run(self):
		self.root.mainloop()
	
	# creates the menu bar at the top
	def menu_bar(self):
		#menu bar must be a subwidget of root
		menubar = Menu(self.root)
		menubar.add_command(label="Enter New Foods", command=self.new_food)
		menubar.add_command(label="Enter Daily Food", command=self.daily_food)
		optionmenu = Menu(menubar, tearoff=0)
		optionmenu.add_command(label="Basic Entry Mode", command=self.set_basic)
		optionmenu.add_command(label="Quick Entry Mode", command=self.set_quick)
		menubar.add_cascade(label="Options", menu=optionmenu)
		
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
	
	# sets program to quick entry mode
	def set_quick(self):
		if not(self.is_quick):
			self.is_quick = True
			# calls the function for the current tab
			self.tab_dict[self.current_tab]()
	
	#sets program to basic entry mode
	def set_basic(self):
		if self.is_quick:
			self.is_quick = False
			# calls the function for the current tab
			self.tab_dict[self.current_tab]()
	
	# sets up the new food tab
	def new_food(self):
		self.current_tab = NEWFOOD
		self.reset_top()
		print("danny boy")
		if self.is_quick:
			self.quick_new_food()
		else:
			self.basic_new_food()
	
	# FINISH ME!!!
	def quick_new_food(self):
		l = Label(self.top, text="Add New Foods")
		#l.grid(row=1,column=1,padx=15,pady=15)
		l.pack()
		
		quick_entry = Entry(self.top)
		quick_entry.pack()
	# FINISH ME!!!
	def basic_new_food(self):
		print("basic new food")
	
	#sets up the daily food tab
	def daily_food(self):
		self.current_tab = DAILYFOOD
		self.reset_top()
		print("bubkis")
		if self.is_quick:
			self.quick_daily_food()
		else:
			self.basic_daily_food()
	
	
	def quick_daily_food(self):
		print("quick daily food")
		
	def basic_daily_food(self):
		print("basic daily food")
		
		
	
if __name__ == "__main__":
	t = TopLevel()
	t.run()