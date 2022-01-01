from sqlalchemy import func

from db import db


class ProductModel(db.Model):
    __tablename__ = "products"

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    photo_url = db.Column(db.String(255), nullable=False)
