from main import app
from models import db, User, Course

db.create_all(app=app)

print('database initialized!')