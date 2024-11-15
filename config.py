from flask_sqlalchemy import SQLAlchemy

# config.py
USER = 'root'
POSSWOED = ''
HOST = 'localhost'
DATABASE ='cursePython'

# configuracion de la base de datos
DATABASE_URI = f'mysql+pymysql://{USER}:{POSSWOED}@{HOST}/{DATABASE}'
db = SQLAlchemy()


















