from django.urls import path
from home import views


urlpatterns = [

    path('',views.home_page, name='home_page'),
    path('success_message',views.success_message, name='page'),
    path('already_exists',views.already_exists, name='already_exists'),
]    