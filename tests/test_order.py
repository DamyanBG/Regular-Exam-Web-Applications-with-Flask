import json
import os
from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from constants import TEMP_FILE_FOLDER
from db import db
from models import OrderModel
from services.s3 import S3Service
from tests.factories import CustomerFactory
from tests.helpers import encoded_stl, generate_token, mock_uuid


class TestOrder(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        self.headers = {"Content-Type": "application/json"}
        return create_app("config.TestApplicationConfiguration")

    @patch("uuid.uuid4", mock_uuid)
    @patch.object(S3Service, "upload_stl", return_value="some-test.url")
    def test_create_order(self, s3_mock):
        url = "/customers/orders"

        data = {
            "title": "Test title",
            "description": "Test description",
            "stl": encoded_stl,
            "address": "ulica Ivan Shishman 27A, grad Dobrich"
        }


        customer = CustomerFactory()
        token = generate_token(customer)
        self.headers.update({"Authorization": f"Bearer {token}"})
        orders = OrderModel.query.all()
        assert len(orders) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        orders = OrderModel.query.all()
        assert len(orders) == 1

        data.pop("stl")

        expected_resp = {
            "pk": orders[0].pk,
            "stl_url": "some-test.url",
            **data
        }

        actual_resp = resp.json
        actual_resp.pop("create_on")
        assert resp.status_code == 201
        assert actual_resp == expected_resp

        stl_name = f"{mock_uuid()}.stl"
        path = os.path.join(TEMP_FILE_FOLDER, stl_name)
        s3_mock.assert_called_once_with(path, stl_name)
