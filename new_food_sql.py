#Joey Smith and Minerva Chen
#12/16/14

import sqlite3

conn = sqlite3.connect("example.db")

c = conn.cursor()

c.execute('''CREATE TABLE foods
             (size real, size_unit text, cals real, vitA real, vit_unit text)''')

def insert_food(size, size_unit, cals, vitA, vit_unit):
	print("gumbosake")
	food = [size, size_unit, cals, vitA, vit_unit]
	c.execute('''INSERT INTO foods VALUES (?, ?, ?, ?, ?)''', food)
	c.execute('SELECT * FROM foods')
	print(c.fetchone())