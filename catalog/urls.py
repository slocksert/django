from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', view=views.product_list, name="product_list"),
    re_path(r'^(?P<slug>[\w_-]+)/$', view=views.category, name="category"),
    re_path(r'^produtos/(?P<slug>[\w_-]+)/$', view=views.product, name="product")
    
]