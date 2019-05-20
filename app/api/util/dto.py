""" Data schemas """

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
        """return the input names as lower case

        Args:
            data (dict): data list with
            many : instructs marshmallow to expect more than one input field

        Returns:
            dict: input fields in lower case
        """

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
    passporturl = fields.Url(required=True, data_key='passportUrl')
    isadmin = fields.Boolean(missing=False, data_key='isAdmin')
    ispolitician = fields.Boolean(missing=False, data_key='isPolitician')


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


class VoteSchemaLoad(BaseSchema):
    """Vote schema for de-serializing vote data input """
    office = fields.Integer()
    candidate = fields.Integer()


class VoteSchemaDump(BaseSchema):
    """ Vote schema for serializing vote data output """
    office = fields.Integer(attribute='office_id')
    candidate = fields.Integer(attribute='candidate_id')
    created_on = fields.LocalDateTime()
    created_by = fields.Integer()


class ResultSchema(BaseSchema):
    """ Office results schema for serializing office results set """
    office = fields.Integer(attribute='office_id')
    candidate = fields.Integer(attribute='candidate_id')
    result = fields.Integer()


class PetitionLoadSchema(BaseSchema):
    """ Petition deserializer schema """
    office = fields.Integer(required=True)
    contested_by = fields.Integer(required=True)
    created_by = fields.Integer(dump_only=True)
    body = fields.String(required=True)
    evidence = fields.List(fields.Url())


class PetitionDumpSchema(BaseSchema):
    """ Petition serializer schema """
    petition_id = fields.Integer(attribute="id")
    office = fields.Integer(attribute="office_id")
    contested_by = fields.Integer()
    created_by = fields.Integer()
    created_on = fields.LocalDateTime()
    body = fields.String()
    evidence = fields.List(fields.Url())


party_schema = PartySchema()
parties_schema = PartySchema(many=True)
office_schema = OfficeSchema()
offices_schema = OfficeSchema(many=True)
user_schema = UserSchema()
auth_schema = AuthSchema()
candidate_load_schema = CandidateSchemaLoad()
candidate_dump_schema = CandidateSchemaDump()
vote_load_schema = VoteSchemaLoad()
vote_dump_schema = VoteSchemaDump()
results_schema = ResultSchema(many=True)
petition_load_schema = PetitionLoadSchema()
petitions_dump_schema = PetitionDumpSchema()
