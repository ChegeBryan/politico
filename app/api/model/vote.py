""" Vote database model and methods """

import datetime as dt


class Vote:
    """ Vote class for and methods for database manipulation """

    def __init__(self, office, candidate):
        self.office = office
        self.candidate = candidate
        self.created_on = dt.datetime.now()

