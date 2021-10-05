from sqlalchemy import create_engine

# TODO read from props file
# Users are required to create the no-gitapp.conf file with the following:
# DB_USER
# DB_PASSWORD
# DB_NAME
engine = create_engine("mysql+pymysql://tobe:propertized@localhost:3600/params")