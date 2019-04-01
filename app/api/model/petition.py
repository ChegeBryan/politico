""" Petition database model and methods """

import datetime as dt


class Petition:
    """Petition class methods that involve reading
    and writing to the database
    """

    def __init__(self, **kwargs):
        self.office = kwargs.get("office")
        self.contested_by = kwargs.get("contested_by")
        self.created_by = kwargs.get("created_by")
        self.body = kwargs.get("body")
        self.evidence = kwargs.get("evidence")
        self.created_on = dt.datetime.now()
