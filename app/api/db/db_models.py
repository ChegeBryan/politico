# database relations.

from passlib.hash import pbkdf2_sha256 as sha256


def drop_tables():
    """  Removes tables form the database (TDD) """
    users = """ DROP TABLE IF EXISTS users """
    blacklist = """ DROP TABLE IF EXISTS blacklist """
    parties = """ DROP TABLE IF EXISTS parties """
    return [users, blacklist, parties]


def create_tables():
    """Create relations in the database"""
    users = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(20) NOT NULL,
        othername VARCHAR(20),
        email VARCHAR(30) NOT NULL,
        phonenumber VARCHAR(24) NOT NULL,
        password VARCHAR(128) NOT NULL,
        passportUrl VARCHAR(256) NOT NULL,
        isAdmin BOOLEAN DEFAULT FALSE,
        isPolitician BOOLEAN DEFAULT FALSE
    );
    """
    blacklist = """
    CREATE TABLE IF NOT EXISTS blacklist (
        id SERIAL PRIMARY KEY,
        token TEXT NOT NULL,
        blacklisted_on TIMESTAMPTZ NOT NULL
    );
    """
    parties = """
    CREATE TABLE IF NOT EXISTS parties (
      id SERIAL PRIMARY KEY,
      party_name VARCHAR(50) NOT NULL,
      hq_address VARCHAR(100) NOT NULL,
      logo_url VARCHAR(256) NOT NULL
    );
    """

    return [users, blacklist, parties]


def add_admin():
    """ Adds an admin user to the table if admin user does not exist """
    hashed_password = sha256.hash('2019NBO37')
    sql = """
    INSERT INTO
     users (firstname, lastname, email, phonenumber, password, passportUrl,
      isadmin)
    SELECT 'admin', 'user', 'admin@politico.org', '11223-123112',
     %s, 'http://admin.url.com', 'True'
    WHERE NOT EXISTS (SELECT isadmin FROM users WHERE isadmin='TRUE');
    """
    query = sql, (hashed_password,)
    return query

