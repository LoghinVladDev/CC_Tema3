from mysql import connector


def get_db_connection():
    return connector.connect(
        host="localhost",
        user="covid-19-user",
        password="covid-19-pass",
        db="CC_T3"
    )
