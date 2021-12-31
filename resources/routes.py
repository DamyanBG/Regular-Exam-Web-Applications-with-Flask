from resources.admin import CreateAdmin, CreateWorker
from resources.auth import Register, Login, LoginAdmin, LoginWorker
from resources.cart import CreateCart, CloseListCart, ListCartForWorkers
from resources.offers import ListCreateOffer, OfferDetail, AcceptOffer, RefuseOffer
from resources.orders import ListCreateOrder, OrderDetail
from resources.products import ListCreateDeleteUpdateProduct

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateOrder, "/customers/orders"),
    (OrderDetail, "/customers/orders/<int:pk_>"),
    (CreateAdmin, "/admins/create-admin"),
    (LoginAdmin, "/admins/login"),
    (CreateWorker, "/workers/create-worker"),
    (LoginWorker, "/workers/login"),
    (ListCreateOffer, "/workers/offers"),
    (OfferDetail, "/workers/offers/<int:pk_>"),
    (AcceptOffer, "/customers/offers/<int:pk_>/accept"),
    (RefuseOffer, "/customers/offers/<int:pk_>/refuse"),
    (ListCreateDeleteUpdateProduct, "/workers/products"),
    (CreateCart, "/workers/products/<int:pk_>/add-to-cart"),
    (CloseListCart, "/customers/cart"),
    (ListCartForWorkers, "/access/cart")
)
