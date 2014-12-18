#Joey Smith and Minerva Chen
#12/16/14

import sqlite3

#creates example.db or connects with it if it exists
conn = sqlite3.connect("example.db")

c = conn.cursor()

#creates a new table if it does not exist yet
c.execute('''CREATE TABLE IF NOT EXISTS foods
             (size real, size_unit text, cals real, vitA real, vit_unit text)''')

def insert_food(size, size_unit, cals, vitA, vit_unit):
	print("gumbosake")
	food = [size, size_unit, cals, vitA, vit_unit]
	c.execute('''INSERT INTO foods VALUES (?, ?, ?, ?, ?)''', food)
	c.execute('SELECT * FROM foods')
	print(c.fetchall())


def save_and_close():
	conn.commit()
	conn.close()