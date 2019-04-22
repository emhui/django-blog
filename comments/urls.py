from django.conf.urls import url
from . import views

app_name='comments'

urlpatterns=[
    url(r'comments/post/([0-9]+)/$',views.post_comment,name='post_comment'),
]