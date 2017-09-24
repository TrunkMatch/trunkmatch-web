from django.conf.urls import url
from rest_auth.tests.urls import FacebookLogin, TwitterLogin

from tm_api.main import example_endpoint

urlpatterns = [
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/twitter/$', TwitterLogin.as_view(), name='twitter_login')
]
