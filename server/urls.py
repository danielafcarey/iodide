from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import server.api.views

urlpatterns = [
    url(r'^$', server.api.views.index, name='index'),
    path('admin/', admin.site.urls),
]
