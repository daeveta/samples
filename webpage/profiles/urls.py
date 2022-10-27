from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('teachers/', views.teachers, name='profiles'),
    path('students/', views.students, name='students'),
    path('student-list/', views.student_list, name='student-list'),
    # path('coder/<int:id>', instance)
]