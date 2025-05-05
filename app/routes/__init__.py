# Importing the 'main' blueprint from the routes module.
# This allows us to register the blueprint in the application factory
# so that all routes and logic defined within this blueprint are included in the application.
from .routes import main