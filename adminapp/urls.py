from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page, name='home_page'),
    path('login_page/',login_page, name='login_page'),
    path('logout_page/',logout_page, name='logout_page'),
    path('signup/', SignUpView.as_view(), name='signup'),

    path('faculty/create/',faculty_create, name='faculty_create'),
    path('faculty/<int:pk>/edit/',faculty_edit, name='faculty_edit'),
    path('faculty/<int:pk>/delete/',faculty_delete, name='faculty_delete'),
    path('faculty/list/',faculty_list, name='faculty_list'),


    path('guruh/create/', guruh_created, name='guruh_create'),
    path('guruh/<int:pk>/edit/', guruh_edit, name='guruh_edit'),
    path('guruh/<int:pk>/delete/', guruh_delete, name='guruh_delete'),
    path('guruh/list/', guruh_list, name='guruh_list'),

    path('subject/create/', subject_created, name='subject_create'),
    path('subject/<int:pk>/edit/', subject_edit, name='subject_edit'),
    path('subject/<int:pk>/delete/', subject_delete, name='subject_delete'),
    path('subject/list/', subject_list, name='subject_list'),

    path('teacher/create/', teacher_create, name='teacher_create'),
    path('teacher/<int:pk>/edit/', teacher_edit, name='teacher_edit'),
    path('teacher/<int:pk>/delete/', teacher_delete, name='teacher_delete'),
    path('teacher/list/', teacher_list, name='teacher_list'),

    path('profile/',profile,name='profile')
]