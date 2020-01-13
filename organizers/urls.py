from django.urls import path
from .views import (organizers,
                    add_dev,
                    add_faculty,
                    add_student,
                    delete_faculty,
                    delete_student,
                    delete_dev,
)
urlpatterns = [
    path('',organizers,name='organizers'),
    path('add_dev/',add_dev,name='add_dev'),
    path('add_faculty/',add_faculty,name='add_faculty'),
    path('add_student/',add_student,name='add_student'),
    path('<int:pk>/delete_faculty',delete_faculty,name='delete_faculty'),
    path('<int:pk>/delete_student',delete_student,name='delete_student'),
    path('<int:pk>/delete_dev',delete_dev,name='delete_dev'),
]