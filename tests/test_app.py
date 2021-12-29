from flask_testing import TestCase

from config import create_app


class TestApplication(TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def create_app(self):
        return create_app("config.TestApplicationConfiguration")