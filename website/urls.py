from django.urls import path
from website.views import *

app_name='website'
urlpatterns = [
    path('',index_home,name='home'),
    path('about',index_about,name='about'),
    path('contact',index_contact,name='contact'),
    path('elements',index_elements,name='elements')
]
