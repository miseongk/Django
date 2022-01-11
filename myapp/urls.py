from django.urls import path
from .views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('student/', StudentListCreateAPIView.as_view()),
    path('student/<student_pk>', StudentRetrieveUpdateDestroyAPIView.as_view())
]