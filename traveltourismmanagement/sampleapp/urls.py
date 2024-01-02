from django.urls import path
from . import views
urlpatterns=[
    path("home",views.home),
    path("addStudent",views.addStudent,name="addStudent"),
    path("insertStudent",views.insertStudent,name="insertStudent"),
    path("contact",views.contact,name="contact"),
    path("viewStudent",views.viewStudents,name="viewStudent"),
]




