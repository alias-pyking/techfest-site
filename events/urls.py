
from django.urls import path
from .views import home,add_event,events,delete_event,add_star,event_detail,register,registered_users_for_event,search_registered_users
urlpatterns = [
    path('',home,name='home'),
    path('add_event/',add_event,name='add_event'),
    path('<int:pk>/',event_detail,name='event_detail'),
    path('<int:pk>/register',register,name='register'),
    path('<int:pk>/registered_users_for_event/',registered_users_for_event,name='registered_users_for_event'),
    path('events/',events,name='events'),
    path('events/<int:id>/delete',delete_event,name='delete_event'),
    path('add_star/',add_star,name='add_star'),
    path('<int:pk>/registered_users_for_event/search/',search_registered_users,name='search_results'),
]