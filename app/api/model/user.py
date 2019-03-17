""" User class methods and model"""
import datetime

import jwt
from instance.config import Config
from passlib.hash import pbkdf2_sha256 as sha256

key = Config.SECRET

class User:
    """  User model class """

    # 1. initialize object with isAdmin and isPolitician set to default False
    # 2. Read the class variable form named arguments **kwargs
    def __init__(self, isAdmin=False, isPolitician=False, **kwargs):
        self.firstname = kwargs.get("firstname")
        self.lastname = kwargs.get("lastname")
        self.othername = kwargs.get("othername")
        self.email = kwargs.get("email")
        self.phonenumber = kwargs.get("phonenumber")
        self.password = kwargs.get("password")
        self.passportUrl = kwargs.get("passportUrl")
        self.isAdmin = isAdmin
        self.isPolitician = isPolitician

    def add_user(self):
        query = """INSERT INTO
          users(firstname, lastname, othername, email, phonenumber, password,
            passportUrl, isAdmin, isPolitician)
          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
          """
        values = (self.firstname, self.lastname, self.othername, self.email,
        self.phonenumber, self.password, self.passportUrl, self.isAdmin,
        self.isPolitician)

        return query, values

    @staticmethod
    def generate_hash_password(password):
        """Method to encrypt password"""
        return sha256.hash(password)

    @staticmethod
    def verify_hash_password(password, hash):
        """Method to decrypt hash password"""
        return sha256.verify(password, hash)

    @staticmethod
    def get_user_by_email(email):
        """ Returns a user found from the database with specified email. """
        sql = """SELECT * FROM users WHERE email=%s"""
        query = sql, (email,)
        return query

    @staticmethod
    def get_user_by_passport(passportUrl):
        """Return user SQL query to a user from database with a certain
        passport url
        """
        sql = """SELECT passportUrl from users WHERE passportUrl=%s"""
        query = sql, (passportUrl,)
        return query

    @staticmethod
    def encode_auth_token(email):
        """Generate auth token

        Args:
            email (string): token identifier
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow()
                   + datetime.timedelta(hours=12),
                'iat': datetime.datetime.utcnow(),
                'sub': email
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """Decode auth token

        Args:
            auth_token (bytes): encoded auth token
        """
        try:
            # decode the token return the email used for enccoding
            payload = jwt.decode(auth_token, key, algorithms='HS256')
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return "Signature expired. PLease login again."
        except jwt.InvalidTokenError:
            return "Invalid token. PLease login again."

