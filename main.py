# python3 script to list down the user detail API'S
from flask import Flask
from db_helper import DB_Helper
import os 
from sqlalchemy.orm import sessionmaker

from insert_user_data import InsertUSerData
from get_user_data import GetUserData

# called `app` in `main.py`.
app = Flask(__name__)
flask_port = os.environ['flask_port']


#################################################	Enter Data into the DB Module  ################################################# 
@app.route('/entry_user_data')
def entry_user_data():
    """ entry camera module API.
    """
    
    module = 'Inserted sucessfully user data'
    engine = DB_Helper().db_connect_sql_alchemy()
    Session = sessionmaker(bind = engine)
    session = Session()

    try :
        InsertUSerData().insert_data(session)
    except :
        module = "Not Able To Insert Entry Camera Module Data"
    session.close()

    return module


#################################################	Get  Data from DB   ################################################# 
@app.route('/get_user_data')
def get_data():
    """ Get User Data API.
    """

    module = 'Retrive Data from the DB'
    engine = DB_Helper().db_connect_sql_alchemy()
    Session = sessionmaker(bind = engine)
    session = Session()

    try :
        name, id = GetUserData().get_info(session)
    except :
        module = 'Not Able To Retrive Data'
    session.close()

    return module
 
 
 ################################################################################################################


if __name__ == '__main__':
	# This is used when running locally only. When deploying to Google App
	# Engine, a webserver process such as Gunicorn will serve the app. This
	# can be configured by adding an `entrypoint` to app.yaml.
	#app.run(host='0.0.0.0', port=flask_port, debug=True)
    app.run(host='0.0.0.0', port=flask_port, debug=True)
	