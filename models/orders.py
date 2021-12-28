from sqlalchemy import func

from db import db


class OrderModel(db.Model):
    __tablename__ = "orders"

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    stl_url = db.Column(db.String(255), nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    address = db.Column(db.String(255), nullable=False)
    customer_pk = db.Column(db.Integer, db.ForeignKey("customers.pk"))
    customer = db.relationship("CustomerModel")
