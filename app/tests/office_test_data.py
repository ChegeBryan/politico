# office dummy test data
from app.api.model.office import Office


# data to use for office test
office = Office('senator', 'congress', False)
office_holder = office.office_jsonified()

invalid_office_name = Office('sene', "congress", False)
invalid_office_name_holder = invalid_office_name.office_jsonified()

invalid_office_type = Office('senator', "cong", False)
invalid_office_type_holder = invalid_office_type.office_jsonified()
