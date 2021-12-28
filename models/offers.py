from sqlalchemy import func

from db import db
from models.enums import State


class OfferModel(db.Model):
    __tablename__ = "offers"

    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(State), default=State.pending, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    order_pk = db.Column(db.Integer, db.ForeignKey("orders.pk"))
    order = db.relationship("OrderModel")
