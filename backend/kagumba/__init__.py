from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/members')
def members():
  return render_template('members.html' , members = members)

@app.route('/contributions')
def contributions():
  pass
