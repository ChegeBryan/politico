# database relations.

from passlib.hash import pbkdf2_sha256 as sha256


def drop_tables():
    """  Removes tables form the database (TDD) """
    users = """ DROP TABLE IF EXISTS users; """
    blacklist = """ DROP TABLE IF EXISTS blacklist; """
    parties = """ DROP TABLE IF EXISTS parties; """
    offices = """ DROP TABLE IF EXISTS offices; """
    candidates = """ DROP TABLE IF EXISTS candidates; """
    votes = """ DROP TABLE IF EXISTS votes; """
    return [votes, candidates, users, blacklist, parties, offices]


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
    offices = """
    CREATE TABLE IF NOT EXISTS offices (
      id SERIAL PRIMARY KEY,
      office_name VARCHAR(50) NOT NULL,
      office_type VARCHAR(50) NOT NULL,
      is_occupied BOOLEAN DEFAULT FALSE
    );
    """
    candidates = """
    CREATE TABLE IF NOT EXISTS candidates (
      office_id INTEGER NOT NULL,
      candidate_id INTEGER NOT NULL,
      party_id INTEGER NOT NULL,
      created_on TIMESTAMPTZ NOT NULL,

      -- define the FK constraints - to ensure the candidate is a a registered
      -- user and the office also exists
      FOREIGN KEY (office_id) REFERENCES offices (id) ON DELETE CASCADE,
      FOREIGN KEY (candidate_id) REFERENCES users (id) ON DELETE CASCADE,
      FOREIGN KEY (party_id) REFERENCES parties (id) ON DELETE CASCADE,

      -- define a composite primary key based on 2 Fields to ensure a candidate
      -- is not registered twice
      CONSTRAINT id PRIMARY KEY (office_id, candidate_id)
    );
    """
    votes = """
    CREATE TABLE IF NOT EXISTS votes(
      office_id INTEGER NOT NULL,
      candidate_id INTEGER NOT NULL,
      created_on TIMESTAMPTZ NOT NULL,
      created_by INTEGER NOT NULL,

      -- define the FK constraints - to ensure the candidate referenced and
      -- office exists in the candidates table
      FOREIGN KEY (office_id, candidate_id) REFERENCES
        candidates (office_id, candidate_id) ON DELETE CASCADE,
      FOREIGN KEY (created_by) REFERENCES users (id) ON DELETE CASCADE,

      -- composite primary key made up 2 fields ensuring a voters vote is not
      -- registered twice
      CONSTRAINT vote_id PRIMARY KEY (office_id, created_by)
    );
    """
    petitions = """
    CREATE TABLE IF NOT EXISTS petitions(
      id SERIAL PRIMARY KEY,
      office_id INTEGER NOT NULL,
      contested_by INTEGER NOT NULL,
      created_by INTEGER NOT NULL,
      body VARCHAR NOT NULL,
      evidence VARCHAR NOT NULL,
      created_on TIMESTAMPTZ NOT NULL,

      -- FK to ensure referential integrity is maintained
      -- disallow deleting a user if they have created a petition
      FOREIGN KEY (office_id, contested_by) REFERENCES
        candidates (office_id, candidate_id) ON DELETE CASCADE,
      FOREIGN KEY (created_by) REFERENCES users (id) ON DELETE RESTRICT
    );
    """

    return [users, blacklist, parties, offices, candidates, votes, petitions]


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
