import os
import uuid

from werkzeug.exceptions import NotFound

from constants import TEMP_FILE_FOLDER
from db import db
from models.products import ProductModel
from services.s3 import S3Service
from utils.helpers import decode_photo

s3 = S3Service()


class ProductsManager:
    @staticmethod
    def get_all():
        return ProductModel.query.all()

    @staticmethod
    def create(product_data):
        photo_name = f"{str(uuid.uuid4())}.{product_data.pop('photo_extension')}"
        path = os.path.join(TEMP_FILE_FOLDER, photo_name)
        decode_photo(product_data.pop("photo"), path)
        photo_url = s3.upload_photo(path, photo_name)
        os.remove(path)
        product_data["photo_url"] = photo_url
        product = ProductModel(**product_data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(offer_data, pk_):
        product_q = ProductModel.query.filter_by(pk=pk_)
        product = product_q.first()
        if not product:
            raise NotFound("This product does not exist")

        product_q.update(offer_data)
        return product

    @staticmethod
    def delete(pk_):
        product_q = ProductModel.query.filter_by(pk=pk_)
        product = product_q.first()
        if not product:
            raise NotFound("This product does not exist")

        db.session.delete(product)
        db.session.commit()
