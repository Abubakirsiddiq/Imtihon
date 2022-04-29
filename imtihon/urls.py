from django.contrib import admin
from django.urls import path
from student.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('/student', student),
    path('/muallif', muallif),
    path('/student<int:son>', student_ochir),
]
