from werkzeug.exceptions import NotFound

from db import db
from models import OfferModel, State


class OfferManager:
    @staticmethod
    def get_all():
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
