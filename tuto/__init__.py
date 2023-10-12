from .app import app
import tuto.views
from flask_sqlalchemy import SQLAlchemy
import tuto.commands
import tuto.models

db = SQLAlchemy(app)