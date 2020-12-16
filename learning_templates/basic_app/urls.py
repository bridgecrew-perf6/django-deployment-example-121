from django.conf.urls import url
from basic_app import views #we can also do from . import views because it is in the same folder.


app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]