from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trans_api$', views.trans_api.as_view(), name='trans_api'),
]
