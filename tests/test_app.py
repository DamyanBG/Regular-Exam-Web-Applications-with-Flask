import json

from flask_testing import TestCase

from config import create_app
from db import db


class TestApplication(TestCase):
    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def create_app(self):
        return create_app("config.TestApplicationConfiguration")

    def test_authentication_missing_auth_header_raises(self):
        # Arrange
        url_methods = [
            ("/customers/orders", "GET"),
            ("/customers/orders", "POST"),
            ("/customers/orders/1", "DELETE"),
            ("/customers/orders/1", "PUT"),
            ("/workers/offers", "GET"),
            ("/workers/offers", "POST"),
            ("/workers/offers/1", "DELETE"),
            ("/workers/offers/1", "PUT"),
        ]

        # Act
        for url, method in url_methods:
            if method == "GET":
                resp = self.client.get(url)
            elif method == "POST":
                resp = self.client.post(url, data=json.dumps({}))
            elif method == "PUT":
                resp = self.client.put(url, data=json.dumps({}))
            else:
                resp = self.client.delete(url)

            # Assert
            assert resp.status_code == 400
            assert resp.json == {"message": "Invalid token"}

    def test_permission_required_endpoints(self):
        # test endpoints for admin
        pass
