from resources.admin import CreateAdmin, CreateWorker
from resources.auth import Register, Login, LoginAdmin, LoginWorker
from resources.orders import ListCreateOrder, OrderDetail

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateOrder, "/customers/orders"),
    (OrderDetail, "/customers/orders/<int:pk_>"),
    (CreateAdmin, "/admins/create-admin"),
    (LoginAdmin, "/admins/login"),
    (CreateWorker, "/workers/create-worker"),
    (LoginWorker, "/workers/login"),
)