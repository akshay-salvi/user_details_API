#  python3 script to initialize the User Details table.

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from db_helper import DB_Helper

engine = DB_Helper().db_connect_sql_alchemy()
Base = declarative_base(bind = engine)

class USERTable(Base):
    """ Declaring user_detials table
    """
    
    __tablename__ = 'user_details'
    __table_args__ = ({"schema": 'public'})
    
    user_id = Column(String)
    user_name = Column(String)
    time_zone = Column(String)
    
    __mapper_args__ = {
        'primary_key':[user_id]
    }
