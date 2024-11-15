from http.cookiejar import debug
from webbrowser import register

from flask import  Flask
from config import  db, DATABASE_URI
from routes.user_routers import user_bp
from router.product_routes import product_bp
from router.store_routes import store_bp

app = flask(__name__)

# cofigurar la base de datos
db.init_app(app)
app-register_blueprint(user_bp)
app-register_blueprint(product_bp)

# crear las tablas si no existen
with app.app_context() :
    db.create_all()

if __name__ == '__main__':
    app.run(debug=true)










from doctest import debug

from app import app

if __name__=="__main__":
    app.run(debug=True)
