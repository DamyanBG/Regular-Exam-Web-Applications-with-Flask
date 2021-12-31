from werkzeug.exceptions import NotFound, BadRequest

from db import db
from models import Status
from models.cart import CartModel


class CartManager:
    @staticmethod
    def get_all():
        return CartModel.query.all()

    @staticmethod
    def create(cart_data, pk_, customer_pk):
        product_pk = pk_
        check_q = CartModel.query.filter_by(customer_pk=customer_pk, product_pk=pk_, status="open")
        check = check_q.first()
        if check:
            raise BadRequest("You already have this product in your cart!")
        cart_data["product_pk"] = product_pk
        cart_data["customer_pk"] = customer_pk
        cart = CartModel(**cart_data)
        db.session.add(cart)
        db.session.commit()
        return cart

    @staticmethod
    def update(cart_data, pk_, customer_pk):
        cart_q = CartModel.query.filter_by(customer_pk=customer_pk, product_pk=pk_, status="open")
        cart = cart_q.first()
        if not cart:
            raise BadRequest("You do not have this product in your cart, please add !")
        cart_q.update(cart_data)
        db.session.add(cart)
        db.session.commit()
        return cart


    @staticmethod
    def finish(customer_pk):
        customer_cart_query = CartModel.query.filter_by(customer_pk=customer_pk)
        customer_cart = customer_cart_query.all()
        if not customer_cart:
            raise NotFound("You do not have cart created")
        customer_cart_query.update({"status": Status.closed})
        for row in customer_cart:
            db.session.add(row)
            db.session.commit()
        return customer_cart

    @staticmethod
    def get_your_cart(customer_pk):
        customer_cart_query = CartModel.query.filter_by(customer_pk=customer_pk)
        customer_cart = customer_cart_query.all()
        if not customer_cart:
            raise NotFound("You do not have cart created")
        return customer_cart
