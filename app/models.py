from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    @classmethod
    def get_by_email(cls, email):
        return User.query.filter_by(email=email).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def authenticate(self, password):
        return self.password == password
