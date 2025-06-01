from app.urls.home import urlpatterns as home_url
from app.urls.auth import urlpatterns as auth_url
from app.urls.order import urlpatterns as order_url
from app.urls.market import urlpatterns as  market_url
from app.urls.threed import urlpatterns as threed_url
from app.urls.konkurs import urlpatterns as konkurs_url
from app.urls.operator import urlpatterns as operator_url
from app.urls.payment import urlpatterns  as payment_url
from app.urls.requests import urlpatterns as request_url
urlpatterns = [
    *home_url , *auth_url , *order_url, *market_url , *threed_url , *konkurs_url, *operator_url , *payment_url,*request_url
]