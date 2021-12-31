from random import randint

import factory

from db import db
from models import CustomerModel, RoleType


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.flush()
        return object


class CustomerFactory(BaseFactory):
    class Meta:
        model = CustomerModel

    pk = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000000, 200000000))
    password = factory.Faker("password")
    role = RoleType.customer
