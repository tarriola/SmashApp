# Import database object from main application module
from app import db

# define the Character model
class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    info = db.Column(db.String(500), nullable=False)
    # upSpecial = db.Column(db.String(500), nullable=True)
    # standSpecial = db.Column(db.String(500), nullable=True)
    # sideSpecial = db.Column(db.String(500), nullable=True)
    # downSpecial = db.Column(db.String(500), nullable=True)
    # entrance = db.Column(db.String(200), nullable=True)
    # grab = db.Column(db.String(200), nullable=True)

    def __init__(self, name, info):
        self.name = name
        self.info = info

    def __repr__(self):
        return '<Character: %r>' % (self.name)
