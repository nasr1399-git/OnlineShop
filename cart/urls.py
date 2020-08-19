from django.urls import path
from django.conf.urls import url
from . import views
app_name = "cart"

urlpatterns = [
    url('', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\w+)/$',views.cart_add,name='cart_add'),
    url(r'^remove/(?p<product_id>\d+)/$',views.cart_remove,name='cart_remove'),   
]