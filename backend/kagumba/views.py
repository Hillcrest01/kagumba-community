@app.py("/home")
def home():
  return render_template("home.html")
