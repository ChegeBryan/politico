from marshmallow import Schema, fields, validate


class PartySchema(Schema):
    """
    Party schema mapped onto Party() class attributes
    """
    party_id = fields.UUID(attribute='_id')
    party_name = fields.String(required=True, validate=[
                               validate.Length(min=4, error="Party name does not meet minimum length of 4 letters."), validate.Regexp(r'[a-zA-Z]', error="Party name cannot contain number(s).")])
    hq_address = fields.String(required=True, validate=[
                               validate.Length(min=1, error="Please provide party Headquarters address.")])


class OfficeSchema(Schema):
    """
    Office schema mapped onto Office() class attributes
    """
    officeId = fields.UUID(attribute='_id')
    officeName = fields.Str(required=True, validate=[validate.OneOf(
        ('president', 'governor', 'senator', 'house of representatives'), error="{input} not a valid office name. Try one of these {choices}.")])
    officeType = fields.Str(required=True, validate=[validate.OneOf(
        ('federal', 'congress', 'state'), error="{input} not a valid office type. Try one of these {choices}.")])
    isOccupied = fields.Boolean(missing=False)


class UserSchema(Schema):
    """
    User schema mapped on User class attributes
    """
    firstname = fields.String(required=True, validate=[validate.Length(
        min=2, error="{input} is not a valid person's name."), validate.Regexp(r'^[a-zA-Z]*$', error="Person name cannot contain number(s).")])
    lastname = fields.String(required=True, validate=[validate.Length(
        min=2, error="{input} is not a valid person's name."), validate.Regexp(r'^[a-zA-Z]*$', error="Person name cannot contain number(s).")])
    othername = fields.String(required=True, validate=[validate.Length(
        min=2, error="{input} is not a valid person's name."), validate.Regexp(r'^[a-zA-Z]*$', error="Person name cannot contain number(s).")])
    email = fields.Email(required=True)
    phonenumber = fields.String(required=True, validate=[validate.Length(
        min=10, error="{input} is not a valid phonename.")])
    password = fields.String(required=True)
    passportUrl = fields.Url(required=True, default="https://api.some.password.org/")
    isAdmin = fields.Boolean(missing=False)
    isPolitician = fields.Boolean(missing=False)



party_schema = PartySchema()
parties_schema = PartySchema(many=True)
office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)
user_schema = UserSchema()
