""" Blacklist_token class method and model """

import datetime


class BlacklistToken:
    """Blacklist token class

    1. initializes the class with the user token and the time created
    """
    def __init__(self, token):
        self.token = token,
        self.blacklisted_on = datetime.datetime.now()

    def add_blacklist_token(self):
        query = """INSERT INTO blacklist(token, blacklisted_on) VALUES (%s, %s);"""
        values = (self.token, self.blacklisted_on)

        return query, values


