""" election results model """


def get_office_result(office):
    """SQL query to read office results from database

    Args:
        office (integer): office id to get results of
        candidate (integer): candidate id to get results of
    """
    sql = """
    SELECT office_id, candidate_id, COUNT(candidate_id) AS result
    FROM votes
    WHERE office_id=%s
    GROUP BY office_id, candidate_id
    ORDER BY result DESC;
    """
    query = sql, (office,)
    return query
