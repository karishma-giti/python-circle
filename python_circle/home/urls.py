from django.urls import path
from home import views

    


urlpatterns = [

    path('',views.insertion, name='insertion'),
    path('validate_username',views.validate_username, name='validate_username'),
    path('success_message',views.success_message, name='success_message'),
    path('user_list',views.user_list,name="user_list"),
]    