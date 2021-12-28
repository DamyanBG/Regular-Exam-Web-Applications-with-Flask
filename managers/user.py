from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.users import CustomerModel, AdministratorModel, WorkerModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = CustomerModel(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server error")
        return user

    @staticmethod
    def login(user_data):
        user = CustomerModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_admin(user_data):
        user = AdministratorModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_worker(user_data):
        user = WorkerModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def create_admin(data):
        data["password"] = generate_password_hash(data["password"])
        admin = AdministratorModel(**data)
        db.session.add(admin)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server error")
        return admin

    @staticmethod
    def create_worker(data):
        data["password"] = generate_password_hash(data["password"])
        worker = WorkerModel(**data)
        db.session.add(worker)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server error")
        return worker
