# Helper Functions, used as common resource for DB connections Entry Exit Camera Module

import os
from sqlalchemy import create_engine


class DB_Helper():
    """ Class helper is creating the connection with DataBase.
    """

    def __init__(self):
        pass
        
    def db_connect_sql_alchemy(self):
        """ creating DB connection using SQl Alchemy.
        """
        engine = create_engine('postgresql://postgres:postgres@localhost:5432/store_data', echo=False)
        
        return engine

