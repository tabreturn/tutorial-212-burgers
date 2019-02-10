from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

MENUDB = 'menu.db'

@app.route('/')
def index():
  con = sqlite3.connect(MENUDB)

  burgers = []
  free = '0'
  #cur = con.execute('SELECT burger,price FROM burgers WHERE price>=' + free)
  cur = con.execute('SELECT burger,price FROM burgers WHERE price>=?', (free,))
  for row in cur:
    burgers.append(list(row))

  drinks = []
  cur = con.execute('SELECT drink,price FROM drinks')
  for row in cur:
    drinks.append(list(row))

  sides = []
  cur = con.execute('SELECT side,price FROM sides')
  for row in cur:
    sides.append(list(row))

  con.close()

  return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)

@app.route('/order')
def order():
  return render_template('order.html')
