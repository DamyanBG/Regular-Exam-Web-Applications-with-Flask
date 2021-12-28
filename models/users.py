from db import db

from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class CustomerModel(BaseUserModel):
    __tablename__ = "customers"

    role = db.Column(db.Enum(RoleType), default=RoleType.customer, nullable=False)


class WorkerModel(BaseUserModel):
    __tablename__ = "workers"

    role = db.Column(db.Enum(RoleType), default=RoleType.worker, nullable=False)


class AdministratorModel(BaseUserModel):
    __tablename__ = "administrators"

    role = db.Column(db.Enum(RoleType), default=RoleType.admin, nullable=False)
