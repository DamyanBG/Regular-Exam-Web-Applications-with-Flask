import json

from flask_testing import TestCase

from config import create_app
from db import db
from models import CustomerModel, RoleType
from tests.helpers import object_as_dict


class TestAuth(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    def test_register_customer(self):

        # Test if a customer is in database when register endpoint is hit.
        # Assure that the role assign is a Customer role.

        url = "/register"

        data = {
            "email": "test@test.com",
            "password": "123456",
            "first_name": "Test",
            "last_name": "Testov",
            "phone": "+359895398744"
        }

        customers = CustomerModel.query.all()
        assert len(customers) == 0

        # Act
        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        # Assert
        assert resp.status_code == 201
        assert "token" in resp.json

        customers = CustomerModel.query.all()
        assert len(customers) == 1
        customer = object_as_dict(customers[0])
        customer.pop("password")
        data.pop("password")

        assert customer == {"pk": customer["pk"], "role": RoleType.customer, **data}

