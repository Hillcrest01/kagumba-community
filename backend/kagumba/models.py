class User(UserMixin, db.Model):
  __tablename__ = 'user'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20) , nullable = False)
  full_name = db.Column(db.String(60), nullable = False)
  password_hash = db.Column(db.String(257), nullable = False)
