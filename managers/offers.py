from werkzeug.exceptions import NotFound

from db import db
from managers.auth import auth
from models import OfferModel, State, RoleType, OrderModel


class OfferManager:
    @staticmethod
    def get_all():
        current_user = auth.current_user()
        if current_user.role == RoleType.customer:
            orders_query = OrderModel.query.filter_by(customer_pk=current_user.pk)
            orders = orders_query.all()
            offer = []
            for order in orders:
                pk = order.pk
                offer_query = OfferModel.query.filter_by(order_pk=pk)
                offer_search = offer_query.first()
                # here there can be added functionality for not offered orders
                offer.append(offer_search)
                a = 5
            return offer
        else:
            return OfferModel.query.all()

    @staticmethod
    def create(offer_data):
        offer = OfferModel(**offer_data)
        db.session.add(offer)
        db.session.commit()
        return offer

    @staticmethod
    def update(offer_data, pk_):
        offer_q = OfferModel.query.filter_by(pk=pk_)
        offer = offer_q.first()
        if not offer:
            raise NotFound("This offer does not exist")

        offer_q.update(offer_data)
        return offer

    @staticmethod
    def delete(pk_):
        offer_q = OfferModel.query.filter_by(pk=pk_)
        offer = offer_q.first()
        if not offer:
            raise NotFound("This offer does not exist")

        db.session.delete(offer)
        db.session.commit()

    @staticmethod
    def accept(pk_):
        offer_q = OfferModel.query.filter_by(pk=pk_)
        offer = offer_q.first()
        if not offer:
            raise NotFound("This offer does not exist")

        offer_q.update({"status": State.accepted})
        db.session.add(offer)
        db.session.commit()
        return offer

    @staticmethod
    def refuse(pk_):
        offer_q = OfferModel.query.filter_by(pk=pk_)
        offer = offer_q.first()
        if not offer:
            raise NotFound("This offer does not exist")

        offer_q.update({"status": State.rejected})
        db.session.add(offer)
        db.session.commit()
        return offer
