import sys
import os

# Ajout du chemin de l'application
sys.path.insert(0, os.path.dirname(__file__))

# Import de l'application
from app import app as application

# Nécessaire pour WSGI
application = application.server