""" User class methods and model"""

from passlib.hash import pbkdf2_sha256 as sha256


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
        query = """INSERT INTO users(firstname, lastname, othername, email,
        phonenumber, password, passportUrl, isAdmin, isPolitician) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);
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
        sql = """SELECT email FROM users WHERE email=%s"""
        query = sql, (email,)
        return query

    @staticmethod
    def get_user_by_passport(passportUrl):
        """Return user SQL query to a user from database with a certain passport
        url """
        sql = """SELECT passportUrl from users WHERE passportUrl=%s"""
        query = sql, (passportUrl,)
        return query

