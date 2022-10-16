import unittest
from sqlalchemy.exc import SQLAlchemyError
from app import create_app, db

test_config = {
    "TESTING": True,
    "SQLALCHEMY_DATABASE_URI": "sqlite:///test_data.db"
}


class TestUser(unittest.TestCase):
    def setUp(self):

        # Create an app instance and create a fresh database
        app = create_app()
        app.config.update(test_config)
        with app.app_context():
            db.drop_all()
            db.create_all()
        self.app = app.test_client()

    @classmethod
    def get_test_data(cls):
        """
        Returns user_credentials
        :return: user_credentials
        """
        return {
            "email": "bhusalsanjeev23@gmail.com",
            "password": "password"
        }

    def register_account(self):
        """
        Register a account.
        :return: test account details
        """
        user_credentials = self.get_test_data()
        result = self.app.post("/register", data=user_credentials)
        return user_credentials

    def test_register(self):
        """
        Test for successfully registration of an account
        :return: None
        """
        user_credentials = TestUser.get_test_data()
        expected_message = "User registered Successfully"
        expected_status_code = 201

        result = self.app.post("/register", data=user_credentials)
        self.assertEqual(result.get_json()["message"], expected_message)
        self.assertEqual(result.status_code, expected_status_code)

    def test_register_email_exist(self):
        """
        Test to check for duplicate email registration
        :return: None
        """
        user_credentials = self.register_account()
        expected_message = "User already exist"
        expected_status_code = 409

        result = self.app.post("/register", data=user_credentials)
        self.assertEqual(result.get_json()["message"], expected_message)
        self.assertEqual(result.status_code, expected_status_code)

    def test_login(self):
        """
        Test for successfully login of an account.
        :return: None
        """
        user_credentials = self.register_account()
        expected_message = "validation successful"
        expected_status_code = 200

        result = self.app.post("/login", data=user_credentials)
        self.assertEqual(result.get_json()["message"], expected_message)
        self.assertEqual(result.status_code, expected_status_code)

    def test_login_password_incorrect(self):
        """
        Test to check for invalid password login
        :return: None
        """
        user_credentials = self.register_account()
        user_credentials["password"] = "incorrect_password"
        expected_message = "Password is incorrect"
        expected_status_code = 403

        result = self.app.post("/login", data=user_credentials)
        self.assertEqual(result.get_json()["message"], expected_message)
        self.assertEqual(result.status_code, expected_status_code)
