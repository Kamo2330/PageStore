from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    path("product/<slug:product_id>/", views.product_detail, name="product"),
    path("cart/", views.cart, name="cart"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
