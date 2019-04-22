from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'archives/(\d{4})/(\d{1,2})',views.archive,name='archives'),
    url(r'category/([0-9]+)',views.category,name='category'),
]
