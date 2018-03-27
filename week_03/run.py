from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

# to run:
# cd to directory
# export FLASK_APP=run.py
# export FLASK_DEBUG=1
# flask run

MENUDB = 'menu.db'

burgers = [
 ['Classic Burger', '$4.99'],
 ['Cheese Burger', '$5.99'],
 ['Chicken Burger', '$5.99'],
 ['Double Burger', '$6.99']
]

drinks = [
 ['Cola', '$0.99'],
 ['Ginger Ale', '$0.99'],
 ['Beer', '$1.99'],
 ['Coffee', '$1.99']
]

sides = [
 ['Fries', '$1.99'],
 ['Onion Rings', '$1.99'],
 ['Mushrooms', '$1.99'],
 ['Salad', '$1.99']
]

@app.route('/')
def index():
  con = sqlite3.connect(MENUDB)
  print(con)
  cur = con.execute('SELECT * FROM burgers')
  print(cur)

  for row in cur:
    #print(row)
    print(row[0]) # id
    print(row[1]) # burger
    print(row[2]) # price

  con.close()

  return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)

@app.route('/order')
def order():
  return render_template('order.html')
