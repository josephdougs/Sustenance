#Joey Smith and Minerva Chen
#12/24/14

import sqlite3

NEWFOODLENGTH = 17

#creates example.db or connects with it if it exists
conn = sqlite3.connect("sus.db")

c = conn.cursor()

#creates a new table if it does not exist yet
c.execute('''CREATE TABLE IF NOT EXISTS foods
             (serv_size real, cals real, cal_unit text, tot_fat real, s_fat real, tr_fat real,
			 p_fat real, m_fat real, cholest real, sodium real, tot_carb real, fiber real, 
			 sugars real, protein real, vit_a real, vit_c real, calcium real, iron real)''')
			 
def insert_food(new_food_list):
	print("gumbosake")
	c.execute('''INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,?)''', new_food_list)
	c.execute('SELECT * FROM foods')
	print(c.fetchall())
	

def save_and_close():
	conn.commit()
	conn.close()