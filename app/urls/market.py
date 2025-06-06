from django.urls import path
from django.conf.urls.static import static

from app.models import Wishlist
from app.views import AuthFormView, HomeListView, ProductListView, UserLogoutView, ProfileListView, RegionFormView, \
    district_list_view, ChangePasswordFormView, WishlistView, ProductOrderDetailView, LikeProductListView, \
ProductOrdersListView, MarketListView
from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path("markets/<str:slug>",MarketListView.as_view(),name="markets"),
    ]