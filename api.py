from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  print ('Hello World')

if __name__ == '__main__':
  app.run()

#test