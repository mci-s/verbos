from flask import Flask
from app.routes import routes
from config import Config

def create_app():
	app = Flask(__name__)

	app.config.from_object(Config)
	app.secret_key = app.config['SECRET_KEY']
    
	app.register_blueprint(routes, url_prefix='/')

	@app.errorhandler(404)
	def page_not_found(error):
		return "This page does not exist", 404
    
	return app