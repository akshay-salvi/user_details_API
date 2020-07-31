#  python3 script to initialize the User Details table.

from sqlalchemy import Column, Integer, String, create_engine, Date, Boolean, LargeBinary, FLOAT, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION


from psycopg2.extensions import adapt, register_adapter, AsIs
import rootpath
import sys

path = rootpath.detect()
sys.path.append(path)


from db_helper import DB_Helper
import datetime

engine = DB_Helper().db_connect_sql_alchemy()
Base = declarative_base(bind = engine)

class USERTable(Base):
    """ Declaring store_entry_table table
    """
    
    __tablename__ = 'user_details'
    __table_args__ = ({"schema": 'public'})
    
    user_id = Column(String)
    user_name = Column(String)
    time_zone = Column(String)
    # start_time = Column(types.DateTime(timezone=True), default=datetime.datetime.utcnow)
    # end_time = Column()
    
    __mapper_args__ = {
        'primary_key':[user_id]
    }
