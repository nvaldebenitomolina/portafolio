from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project1', views.project1, name='project1'),
    path('project2', views.project2, name='project2'),
    path('project3', views.project3, name='project3'),
    path('project4', views.project4, name='project4'),
    path('project5', views.project5, name='project5'),
    path('project6', views.project6, name='project6'),
    path('challenge1', views.challenge1, name='challenge1'),
    path('challenge2', views.challenge2, name='challenge2'),
    path('challenge3', views.challenge3, name='challenge3'),
    path('challenge4', views.challenge4, name='challenge4'),
    path('challenge5', views.challenge5, name='challenge5'),
]
