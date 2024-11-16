from flask import Flask
from config import  db, DATABASE_URI
from routes.user_routes import user_bp


app = Flask(__name__)

#Configurar la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inicializar la base de datos
db.init_app(app)

#Registrar los Blueprints de las rutas
app.register_blueprint(user_bp)

# crear las tablas si no existen
with app.app_context() :
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)










from doctest import debug

from app import app

if __name__=="__main__":
    app.run(debug=True)
