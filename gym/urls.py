from django.urls import path
from . import views

urlpatterns = [
    path('', views.practice_list_view, name='practice_list'),
    path('add/', views.add_practice, name='practice_add'),
    path('<int:p_id>/', views.practice_detail, name='practice_detail'),
    path('<int:p_id>/<int:exe_id>/complete', views.exercises_complete, name='exercises_complete'),
    path('<int:p_id>/<int:exe_id>/incomplete', views.exercises_incomplete, name='exercises_incomplete'),
    path('<int:p_id>/add-ex/', views.add_exercises, name='add_exercises'),

]
