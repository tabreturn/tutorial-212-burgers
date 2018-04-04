from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# to run:
# cd to directory
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

MENUDB = 'menu.db'

def fetchMenu(con):
  burgers = []
  free = '0'
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

  return {'burgers':burgers, 'drinks':drinks, 'sides':sides}

@app.route('/')
def index():
  con = sqlite3.connect(MENUDB)
  menu = fetchMenu(con)
  con.close()
  return render_template('index.html', disclaimer='may contain traces of nuts', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'])

@app.route('/order')
def order():
  con = sqlite3.connect(MENUDB)
  menu = fetchMenu(con)
  con.close()
  return render_template('order.html', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'])

@app.route('/confirm', methods=['POST'])
def confirm():
  details = {}
  items = {}

  for input in request.form:
    if input == 'name' or input == 'address':
      details[input] = request.form[input]
    elif request.form[input] and request.form[input] != '0':
      items[input] = request.form[input]

  con = sqlite3.connect(MENUDB)
  cur = con.execute( 'INSERT INTO orders(name, address, items) VALUES(?, ?, ?)', (details['name'], details['address'], str(items)) )
  con.commit()
  con.close()

  return render_template('confirm.html', details=details, items=items)

@app.route('/vieworder/<order_id>')
def viewOrder(order_id):
  con = sqlite3.connect(MENUDB)
  cur = con.execute('SELECT * FROM orders WHERE id=?', (order_id,))
  order = cur.fetchone()
  con.close()

  return str(order)
