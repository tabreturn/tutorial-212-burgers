from flask import Flask, render_template

app = Flask(__name__)

# to run:
# cd to directory
# export FLASK_APP=run.py
# export FLASK_DEBUG=1
# flask run

@app.route('/')
def index():
  return render_template('index.html', disclaimer='may contain traces of nuts')
