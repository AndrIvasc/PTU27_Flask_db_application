from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Projektas(db.Model):
    __tablename__ = "projektas"
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    kaina = db.Column(db.Float)
    sukurimo_data = db.Column(db.DateTime, default=datetime.datetime.now)

    @property
    def kaina_su_pvm(self): # paskaiciojamas virtualus laukas
        return round(self.kaina * 1.21, 2)

    def __repr__(self):
        return f"ID: {self.id}, {self.pavadinimas}, {self.kaina}, {self.sukurimo_data}"