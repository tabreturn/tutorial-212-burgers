from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>212 Burgers</h1>'

if __name__ == '__main__':
  app.run(debug=True)
