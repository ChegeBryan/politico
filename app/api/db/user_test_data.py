# data to use for user tests
user = {
    "firstname": "peter",
    "lastname": "john",
    "othername": "simon",
    "email": "email@exampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://apps.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_same_email = {
    "firstname": "peter",
    "lastname": "john",
    "othername": "simon",
    "email": "email@exampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://apis.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_same_passport = {
    "firstname": "peter",
    "lastname": "john",
    "othername": "simon",
    "email": "email2@exampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://apps.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_null_values = {
    "firstname": "",
    "lastname": "",
    "othername": "",
    "email": "exam@email.com",
    "phonenumber": "",
    "password": "",
    "passportUrl": "https://ffi.cnc.com"
}

user_names_integer = {
    "firstname": "peter3",
    "lastname": "john2",
    "othername": "si2mon",
    "email": "email@exampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://apps.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_invalid_email = {
    "firstname": "peter",
    "lastname": "john",
    "othername": "simon",
    "email": "emaexampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://apps.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_invalid_passporturl = {
    "firstname": "peter",
    "lastname": "john",
    "othername": "simon",
    "email": "emae@xampl.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "apps.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}

user_logins = {
    "email": "email@exampl.com",
    "password": "some_passowrd"
}

user_malformed_login_email = {
    "email": "emila.sk.cl",
    "password": "some_password"
}

user_no_email = {
    "password": "some_password"
}
user_no_password = {
    "email": "eamil@domain.com",
}

user_no_fields = {

}

admin_login = {
    "email": "admin@politico.org",
    "password": "2019NBO37"
}

user_2 = {
    "firstname": "another",
    "lastname": "user",
    "othername": "test",
    "email": "user@test.com",
    "phonenumber": "23903-39920-221",
    "password": "some_passowrd",
    "passportUrl": "https://test.cn.com",
    "isAdmin": "False",
    "isPolitician": "False"
}
