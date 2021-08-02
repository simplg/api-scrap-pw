import os
from flask import Flask
import yaml

from .controllers import main_controller

def create_app(test_config=None):
    # On initialise l'app flask
    app = Flask(__name__, instance_relative_config=True)
    # Configuration de l'application
    # On récupère en premier la configuration d'un fichier config.yaml présent dans /instance/config.yml
    # Tout d'abord on vérifie que le fichier config.yml est bien présent dans le dossier instance
    if os.path.isfile(app.instance_path + "/config.yml"):
        # S'il est présent, on charge la configuration de celui-ci dans l'app flask
        app.config.from_file("config.yml", load=yaml.load)
    else:
        # Au cas où il n'existe pas, on avertit que celui-ci n'est pas présent
        app.logger.warning(
            "Aucun fichier config.yml n'est présent dans le dossier /instance/. L'application risque de mal fonctionner !"
        )

    # Dans le cas de tests, on passe directement la configuration à create_app, la config de test doit donc remplacer toutes les configs précédentes
    if test_config is not None:
        app.config.from_mapping(test_config)
    
    app.register_blueprint(main_controller)

    return app