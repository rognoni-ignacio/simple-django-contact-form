from django.conf.urls import url

from contactform.views import ContactView

urlpatterns = [
    url(r'^$', view=ContactView.as_view(), name='contact'),
]