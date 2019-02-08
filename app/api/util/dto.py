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


class OfficeSchema(Schema):
    """
    Office schema mapped onto Office() class attributes
    """
    officeId = fields.UUID()
    officeName = fields.Str(required=True, validate=[validate.OneOf(
        ('president', 'governor', 'senator', 'house of representatives'), error="{input} not a valid office name. Try one of these {choices}.")])
    officeType = fields.Str(required=True, validate=[validate.OneOf(
        ('federal', 'congress', 'state'), error="{input} not a valid office type. Try one of these {choices}.")])
    isOccupied = fields.Boolean(missing=False)


party_schema = PartySchema()
parties_schema = PartySchema(many=True)
office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)
