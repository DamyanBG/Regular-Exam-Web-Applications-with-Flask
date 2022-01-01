from sqlalchemy import func

from db import db
from models.enums import Status, Shipped


class CartModel(db.Model):
    __tablename__ = "cart"

    pk = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    customer_pk = db.Column(db.Integer, db.ForeignKey("customers.pk"))
    customer = db.relationship("CustomerModel")
    product_pk = db.Column(db.Integer, db.ForeignKey("products.pk"))
    product = db.relationship("ProductModel")
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Enum(Status), default=Status.open)
    address = db.Column(db.String(255))
    shipped = db.Column(db.Enum(Shipped), default=Shipped.no)

