from resources.auth import Register, Login
from resources.orders import ListCreateOrder

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateOrder, "/customers/orders"),
)