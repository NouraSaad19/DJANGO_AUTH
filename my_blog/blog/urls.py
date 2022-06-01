from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('detail/<int:post_id>',views.post_detail,name='detail'), #post_id from viwes
    path('newpost/',views.PostCreateView.as_view(),name='newpost'),


]