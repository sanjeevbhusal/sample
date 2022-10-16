import unittest
from sqlalchemy.exc import SQLAlchemyError
from app import create_app, db


class TestUser(unittest.TestCase):
    pass
    # def setup(self):
    #     app = create_app()
    #     app.config["TESTING"] = True
    #     app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_data.db"
    #     with app.app_context():
    #         db.drop_all()
    #         db.create_all()
    #     self.app = app.test_client()
    #
    # def test_register(self):
    #     data = {
    #         "email": "bhusalsanjeev23@gmail.com",
    #         "password": "password"
    #     }
    #     result = self.app.post("/register", data=data)
    #     expected_message = "User registered Successfully"
    #     self.assertEqual(result["message"], expected_message)
    #
    # def test_bad_register(self):
    #     data = {
    #         "email": "bhusalsanjeev23@gmail.com",
    #         "password": 12345
    #     }
    #     with self.assertRaises(SQLAlchemyError):
    #         self.app.post("/register", data=data)

    # def login(self):
    #     result = self.app.post("/register", data={
    #         "email": "bhusalsanjeev23@gmail.com",
    #         "password": "password"
    #     })
    #     expected_message = "validation successful"
    #     self.assertEqual(result["message"], expected_message)