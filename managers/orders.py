import os
import uuid

from werkzeug.exceptions import NotFound

from constants import TEMP_FILE_FOLDER
from db import db
from managers.auth import auth
from models import RoleType
from models.orders import OrderModel
from services.s3 import S3Service
from utils.helpers import decode_stl

s3 = S3Service()


class OrdersManager:
    @staticmethod
    def get_all():
        current_user = auth.current_user()
        if current_user.role == RoleType.customer:
            query = OrderModel.query.filter_by(customer_pk=current_user.pk)
        else:
            query = OrderModel.query.all()
        return query

    @staticmethod
    def create(order_data, customer_pk):

        # The function creates file in TEMP_FILE_FOLDER with uuid name, upload it to S3 bucket and delete the file.
        # After that it records the data in the OrderModel database (orders table)

        stl_name = f"{str(uuid.uuid4())}.stl"
        path = os.path.join(TEMP_FILE_FOLDER, stl_name)
        decode_stl(order_data.pop("stl"), path)
        stl_url = s3.upload_stl(path, stl_name)
        os.remove(path)
        order_data["stl_url"] = stl_url
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
