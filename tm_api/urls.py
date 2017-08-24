from django.conf.urls import url

from tm_api.main import example_endpoint

urlpatterns = [
    url(r'^api/v1/hello/$', example_endpoint, name='sign S3'),
]
