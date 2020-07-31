# python3 script to insert the data into the db.

import json
from user_table import USERTable

class InsertUSerData():
    """ Insert Data into the DB.
    
    """
    def __init__(self):
        pass

    def insert_data(self, session):
        """ Read data from the json file
            process it and insert into the DB.
            
            Argument : session
                 
            Returns :
                module : Data inserted sucessfully.
        """
        user_id_data = []
        user_name_data = []
        time_zone_data = []
        activity_periods_data = []

        # process user data
        with open('Test JSON.json', 'r') as j:
            json_data = json.load(j) 
            data = json_data["members"]
            for i in data:
                
                for key, values in i.items():
                    # print(key, values)
                    if key == "id":
                        user_id_data.append(values)
                    elif key == "real_name":
                        user_name_data.append(values)
                        
                    elif key == "tz":
                        time_zone_data.append(values)
                    
                    elif key == "activity_periods":
                        activity_periods_data.append(values)
        
        # insert data into the DB
        for val in range(0, len(user_id_data)):
            
            insert_entry_query = USERTable(user_id = user_id_data[val],
                                                    user_name = user_name_data[val], 
                                                    time_zone = time_zone_data[val])
            insert_entry_data = session.add(insert_entry_query)

            session.commit()
        module = "data inserted sucessfully"
            
        return module
    
