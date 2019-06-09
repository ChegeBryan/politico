""" Applications database model and methods """

import datetime


class Application:
    """Application class for and methods for database manipulation
    """

    def __init__(self, party, office):
        """application class properties registered when an instance of this
        class is created

        Args:
            party (int): id of a registered party
            office (int): id of a registered office
        """
        self.party = party
        self.office = office
        self.requested_on = datetime.datetime.now()
