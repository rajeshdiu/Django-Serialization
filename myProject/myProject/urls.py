
from django.contrib import admin
from django.urls import path
from myProject import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("student/<str:pk>", views.studentDetails),
    path("studentList", views.studentList),
]
