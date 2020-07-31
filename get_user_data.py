# python script to get data of user from the Database.

from sqlalchemy import Sequence, select

from user_table import USERTable
from user_table import USERTable

class GetUserData():
    """ Get user Data from the DB.
    """
    def __init__(self):
        pass
    
    def get_info(self, session):
        """ get user details
            Argument : 
                session :
            Return :
                name_list : names of user
                id_list : id's of user
                
        """
        name_list = []
        id_list = []
        
        result = session.query(USERTable).all()
    
        for row in result:
            name_list.append(row.user_name)
            id_list.append(row.user_id)
        
        return name_list, id_list
    


        