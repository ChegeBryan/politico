from marshmallow import Schema, fields, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class PartySchema(ma.Schema):
    """
    Party schema mapped onto Party() class attributes
    """
    party_id = fields.UUID()
    party_name = fields.String(required=True, validate=[
                               validate.Length(min=4, error="Party name does not meet minimum length of 4 letters."), validate.Regexp(r'[a-zA-Z]', error="Party name cannot contain number(s).")])
    hq_address = fields.String(required=True, validate=[
                               validate.Length(min=1, error="Please provide party Headquarters address.")])


party_schema = PartySchema()


