from werkzeug.exceptions import NotFound

from db import db
from managers.auth import auth
from models.orders import OrderModel


class OrdersManager:
    @staticmethod
    def get_all():
        return OrderModel.query.all()

    @staticmethod
    def create(order_data, customer_pk):
        order_data["customer_pk"] = customer_pk
        order = OrderModel(**order_data)
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def update(order_data, pk_):
        order_q = OrderModel.query.filter_by(pk=pk_)
        order = order_q.first()
        if not order:
            raise NotFound("This order does not exist")
        user = auth.current_user()

        if not user.pk == order.customer_pk:
            raise NotFound("This order does not exist")

        order_q.update(order_data)
        return order

    @staticmethod
    def delete(pk_):
        order_q = OrderModel.query.filter_by(pk=pk_)
        order = order_q.first()
        if not order:
            raise NotFound("This order does not exist")

        db.session.delete(order)
        db.session.commit()
