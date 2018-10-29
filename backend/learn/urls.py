from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_dict_list$', views.get_dict_list.as_view(), name='get_dict_list'),
    url(r'^get_score$', views.get_score.as_view(), name='get_score'),
]
