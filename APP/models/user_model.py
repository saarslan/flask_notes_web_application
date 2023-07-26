from APP import db, bcrypt
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):

    def get_formatted_time():

        current_time = func.now()

        formatted_time = current_time.strftime("%H:%M:%S")

        return formatted_time


    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default = get_formatted_time, nullable=False)

    notes = db.relationship("Note", back_populates="usuario", lazy="dinamic")

    def __init__(self, email, password, full_name):
        self.email = email
        self.password = password
        self.full_name = full_name

    
    def generate_encrypted_password(self):
        self.password = bcrypt.generate_password_hash(self.password)
    
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)