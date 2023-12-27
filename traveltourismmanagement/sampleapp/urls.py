from django.urls import path
from . import views
urlpatterns=[
    path("",views.home),
    path("addStudent",views.addStudent,name="addStudent"),
    path("insertStudent",views.insertStudent,name="insertStudent")
]