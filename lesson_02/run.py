from flask import Flask, render_template

app = Flask(__name__)

# to run:
# cd to directory
# source env/bin/activate
# export FLASK_APP=run.py; export FLASK_DEBUG=1
# flask run

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
  return render_template('index.html', disclaimer='may contain traces of nuts', burgers=burgers, drinks=drinks, sides=sides)

@app.route('/order')
def order():
  return render_template('order.html')
