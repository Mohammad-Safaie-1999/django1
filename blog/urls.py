from django.urls import path
from blog.views import * 

app_name='blog'
urlpatterns = [
    path('',index_home_blog,name='home'),
    path('<int:pid>',index_single,name='single')
]
