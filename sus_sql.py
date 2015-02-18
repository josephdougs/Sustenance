#Joey Smith and Minerva Chen
#12/24/14

import sqlite3

NEWFOODLENGTH = 17

#creates example.db or connects with it if it exists
conn = sqlite3.connect("sus.db")

c = conn.cursor()

#creates a new table if it does not exist yet
c.execute('''CREATE TABLE IF NOT EXISTS foods
             (name text, serv_size real, cals real, tot_fat real, s_fat real, tr_fat real,
			 p_fat real, m_fat real, cholest real, sodium real, tot_carb real, fiber real, 
			 sugars real, protein real, vit_a real, vit_c real, calcium real, iron real)''')
	
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
	return c.fetchone()
	

def save_and_close():
	conn.commit()
	conn.close()