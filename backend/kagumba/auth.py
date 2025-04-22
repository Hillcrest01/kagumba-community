@app.route('/signup')
def signup():
  if form.validate_on_submit():
    name = name,
    password = password
    new_user = (name = name, password = password)
    db.session.add(new_user)
    db.session.commit()
    print("user successfully registered")
    flash("successfully signed up,please log in" , success)
