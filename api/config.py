import os

prod_info ={
    "UPLOAD_FOLDER": "./stg_dir",
    "ip": "192.168.1.44",
    "login": "myapp",
    "password": "aunriseqvoa",
    "feature_data_dir": "./feature_data"
}

dev_info={
    "UPLOAD_FOLDER": "C:\\Users\\maitreyee\\Documents\\\\Shikhya\\Code\\projects\\stg_dir",
    "ip": "127.0.0.1",
    "login": "root",
    "password": "root",
     "feature_data_dir": "C:\\Users\\maitreyee\\Documents\\Shikhya\\Code\\projects\\feature_data"

}

def get_config():
    environment = os.environ['PYTHON_ENV'] or 'dev'
    if environment == 'dev':
        return dev_info
    else:
        return prod_info
