from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'spedanalytics.core.views.home'),
    url(r'^admin/', include(admin.site.urls)),
]
