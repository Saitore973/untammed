from django import urls
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home),
    path('account/register/', views.UserCreateView.as_view(),name="register"),
    path('account/login/', obtain_auth_token ,name="login"),
    path('account/logout/', views.LogoutUsers.as_view() ,name="logout"),
    path('profiles/all/', views.ProfileViewGet.as_view(),name="getprofile"),
    path('profile/update/<int:pk>/', views.ProfileViewUpdate.as_view(),name="updateprofile"),
    path('events/all/', views.EventViewGet.as_view(),name="getevents"),
    path('event/create/', views.EventViewPost.as_view(),name="postevent"),
    path('event/update/<int:id>/', views.EventViewUpdate.as_view(),name="updateevent"),
    path('event/delete/<int:id>/', views.EventViewDelete.as_view(),name="deleteevent"),
]