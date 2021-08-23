from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__,template_folder='templates')

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #Initializing flask extensions
    bootstrap.init_app(app)

    #Registering blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    from .requests import configure_request
    configure_request(app)

    return app