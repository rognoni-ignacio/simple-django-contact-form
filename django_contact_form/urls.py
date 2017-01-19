from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^$', views.Index.as_view(), name='index'),

    # Using this Url configuration to maximize the app encapsulation
    url(r'^$', include('contactform.urls')),

    url(r'^admin/', admin.site.urls),
]
