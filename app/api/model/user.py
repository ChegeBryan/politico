""" User class methods and model"""

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
