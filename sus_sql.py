#Joey Smith and Minerva Chen
#12/24/14

import sqlite3

NEWFOODLENGTH = 17

#creates example.db or connects with it if it exists
conn = sqlite3.connect("sus.db")

c = conn.cursor()

#creates a new table if it does not exist yet
c.execute('''CREATE TABLE IF NOT EXISTS foods
             (name TEXT, serv_size REAL, cals REAL, tot_fat REAL, s_fat REAL, tr_fat REAL,
			 p_fat REAL, m_fat REAL, cholest REAL, sodium REAL, tot_carb REAL, fiber REAL, 
			 sugars REAL, protein REAL, vit_a REAL, vit_c REAL, calcium REAL, iron REAL)''')
			 
 # amount should be saved in number of servings
c.execute('''CREATE TABLE IF NOT EXISTS daily_food
             (year INTEGER, month INTEGER, day INTEGER, food TEXT, amount REAL)''')
	
# inserts all the new foods into the foods table	
def insert_new_food(new_food_list):
	print("gumbosake")
	new_food_list[0] = new_food_list[0].lower() # makes all sql entries lowercase
	c.execute('''INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?, ?, ?)''', new_food_list)
	c.execute('SELECT * FROM foods')
	print(c.fetchall())
	
# returns a tuple containing the data on the given food
def get_food(food_name):
	food_name = food_name.lower()
	print("getting the food")
	print(food_name, "insql")
	# food_name must be in a tuple because otherwise it (being a string) will be seen as a list
	c.execute('''SELECT * FROM foods WHERE name=?''', (food_name,))
	return c.fetchone() # each food should have a unique name

# deletes a food from the food table
def delete_food(food_name):
	food_name = food_name.lower()
	print("deleting the food")
	print(food_name, "insql")
	# food_name must be in a tuple because otherwise it (being a string) will be seen as a list
	c.execute('''DELETE FROM foods WHERE name=?''', (food_name,))
	
# adds a food and amount to the daily_food table
def add_daily_food(year, month, day, food, amount):
	print("adding daily food")
	values = [year, month, day, food, amount]
	print(values)
	print(list(map(type,values)))
	c.execute('''INSERT INTO daily_food VALUES (?, ?, ?, ?, ?)''', values)
	c.execute('SELECT * FROM daily_food')
	print(c.fetchall())
	
	
def test():
	c.execute('''SELECT * FROM foods WHERE ''')

def save_and_close():
	conn.commit()
	conn.close()