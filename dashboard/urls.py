from django.urls import path
from .views import (
    FacultyListCreateAPIView, FacultyDetailAPIView,
    GroupListCreateAPIView, GroupDetailAPIView,
    KafedraListCreateAPIView, KafedraDetailAPIView,
    SubjectListCreateAPIView, SubjectDetailAPIView,
    TeacherListCreateAPIView, TeacherDetailAPIView,
    StudentListCreateAPIView, StudentDetailAPIView
)

urlpatterns = [
    path('faculties/', FacultyListCreateAPIView.as_view(), name='faculty-list-create'),
    path('faculties/<int:pk>/', FacultyDetailAPIView.as_view(), name='faculty-detail'),

    path('groups/', GroupListCreateAPIView.as_view(), name='group-list-create'),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name='group-detail'),

    path('kafedras/', KafedraListCreateAPIView.as_view(), name='kafedra-list-create'),
    path('kafedras/<int:pk>/', KafedraDetailAPIView.as_view(), name='kafedra-detail'),

    path('subjects/', SubjectListCreateAPIView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectDetailAPIView.as_view(), name='subject-detail'),

    path('teachers/', TeacherListCreateAPIView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name='teacher-detail'),

    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailAPIView.as_view(), name='student-detail'),
]