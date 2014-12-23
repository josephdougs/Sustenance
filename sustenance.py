#Joey Smith and Minerva Chen
#12/17/14

from tkinter import *

# a top level class used to keep things organized
class TopLevel:
	
	def __init__(self):
		self.root = Tk()
		#sets size of window to 800px by 800px
		self.root.geometry("800x800")
		#sets the title bar text
		self.root.wm_title("Sustenance")
		
		self.is_quick = False
		self.menu_bar()
	
	# runs the gui code
	def run(self):
		self.root.mainloop()
	
	# creates the menu bar at the top
	def menu_bar(self):
		menubar = Menu(self.root)
		
		menubar.add_command(label="Enter New Foods", command=self.new_food)
		menubar.add_command(label="Enter Daily Info", command=self.hello)
		
		#filemenu = Menu(menubar, tearoff=0)
		#filemenu.add_command(label="Open", command=self.hello)
		#filemenu.add_command(label="Save", command=self.hello)
		#filemenu.add_separator()
		#filemenu.add_command(label="Exit", command=self.root.quit)
		#menubar.add_cascade(label="Options", menu=filemenu)
		optionmenu = Menu(menubar, tearoff=0)
		optionmenu.add_command(label="Basic Entry Mode", command=self.set_basic)
		optionmenu.add_command(label="Quick Entry Mode", command=self.set_quick)
		menubar.add_cascade(label="Options", menu=optionmenu)
		
		
		
		
		self.root.config(menu=menubar)
	
	def hello(self):
		print("hello")	
	
	def fellow(self):
		print("fellow")
	
	# sets program to quick entry mode
	def set_quick(self):
		self.is_quick = True
		print(self.is_quick)
	
	#sets program to basic entry mode
	def set_basic(self):
		self.is_quick = False
		print(self.is_quick)
	
	def new_food(self):
		print("bubkis")
		if self.is_quick:
			self.quick_new_food
		else:
			self.basic_new_food
	
	# FINISH ME!!!
	def quick_new_food(self):
		self.root.wm_title("bubububu")
		l = Label(self.root, text="Add New Foods")
		l.grid(row=1,column=1,padx=15,pady=15)
		
		quick_entry = Entry(self.root)
		
	# FINISH ME!!!
	def basic_new_food(self):
		print("basic new food")
		
if __name__ == "__main__":
	t = TopLevel()
	t.run()