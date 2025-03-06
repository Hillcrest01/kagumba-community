from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Kagumba Community!"

if __name__ == '__main__':
    app.run(debug=True)