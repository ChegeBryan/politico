from marshmallow import Schema, fields
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class PartySchema(ma.Schema):
    """
    Party schema mapped onto Party() class attributes
    """
    party_id = fields.UUID(dump_only=True)
    party_name = fields.String(required=True)
    hq_address = fields.String(required=True)


party_schema = PartySchema()


