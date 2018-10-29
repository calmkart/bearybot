from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^translate/', include('translate.urls', namespace='translate')),
    url(r'^learn/', include('learn.urls', namespace='learn')),
    # url(r'^pk/', include('pk.urls', namespace='pk')),
]

urlpatterns += staticfiles_urlpatterns()
