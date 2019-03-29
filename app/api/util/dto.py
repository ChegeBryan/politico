from marshmallow import Schema, fields, validate, pre_load


class BaseSchema(Schema):
    """ Schema options that are universal to all schema classes """

    class Meta:
        """Schema options"""
        # maintains the field ordering on output
        ordered = True


class PartySchema(BaseSchema):
    """
    Party schema mapped onto Party() class attributes
    """
    party_id = fields.Integer(dump_only=True, attribute='id')
    party_name = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=4,
                error="Party name does not meet minimum length of 4 letters."),
            validate.Regexp(
                r'[a-zA-Z]',
                error="Party name cannot contain number(s).")])
    hq_address = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=1,
                error="Please provide party Headquarters address.")])
    logo_url = fields.URL(required=True)


class OfficeSchema(BaseSchema):
    """
    Office schema mapped onto Office() class attributes
    """
    office_id = fields.Integer(dump_only=True, attribute='id')
    office_name = fields.Str(
        required=True,
        validate=[
            validate.OneOf(
                ('president', 'governor', 'senator',
                 'house of representatives'),
                error="{input} not a valid office name. Try one of these {choices}.")
        ]
    )
    office_type = fields.Str(
        required=True,
        validate=[
            validate.OneOf(
                ('federal', 'congress', 'state'),
                error="{input} not a valid office type. Try one of these {choices}.")
        ]
    )
    is_occupied = fields.Boolean(missing=False)

    @pre_load(pass_many=True)
    def lower_cased(self, data, many):
        data["office_name"] = data["office_name"].lower()
        data["office_type"] = data["office_type"].lower()
        return data


class UserSchema(BaseSchema):
    """
    User schema mapped on User class attributes
    """
    firstname = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=2,
                error="{input} is not a valid person's name."),
            validate.Regexp(
                r'^[a-zA-Z]*$',
                error="Person name cannot contain number(s).")])
    lastname = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=2,
                error="{input} is not a valid person's name."),
            validate.Regexp(
                r'^[a-zA-Z]*$',
                error="Person name cannot contain number(s).")])
    othername = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=2,
                error="{input} is not a valid person's name."),
            validate.Regexp(
                r'^[a-zA-Z]*$',
                error="Person name cannot contain number(s).")])
    email = fields.Email(required=True)
    phonenumber = fields.String(
        required=True,
        validate=[
            validate.Length(
                min=10,
                error="{input} is not a valid phonename.")])
    password = fields.String(required=True)
    passportUrl = fields.Url(required=True)
    isAdmin = fields.Boolean(missing=False)
    isPolitician = fields.Boolean(missing=False)


class AuthSchema(BaseSchema):
    """
    User login data schema
    """
    email = fields.Email(required=True)
    password = fields.String(required=True)


class CandidateSchemaLoad(Schema):
    """
    Candidate schema mapped onto Candidate class attributes
    """
    candidate = fields.Integer(required=True)
    party = fields.Integer(required=True)


class CandidateSchemaDump(BaseSchema):
    """
    Candidate schema dump mapped onto database attributes
    """
    candidate = fields.Integer(attribute='candidate_id')
    office = fields.Integer(attribute='office_id')
    party = fields.Integer(attribute='party_id')
    registered_on = fields.LocalDateTime(attribute='created_on')


party_schema = PartySchema()
parties_schema = PartySchema(many=True)
office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)
user_schema = UserSchema()
auth_schema = AuthSchema()
candidate_load_schema = CandidateSchemaLoad()
candidate_dump_schema = CandidateSchemaDump()
