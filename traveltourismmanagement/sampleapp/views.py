from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def home(request):
    return render(request,'home.html')
def addStudent(request):
    return render(request,"addStudent.html")
def insertStudent(request):
    sid=int(request.POST['sid'])
    sname=request.POST['sname']
    st=Student(sid=sid,sname=sname)
    Student.save(st)
    return render(request,'display.html')
def contact(request):
    return render(request,"contact.html")
def viewStudents(request):
    students =Student.objects.all()
    return render(request,'studentlist.html',{"students":students})
def deleteStudent(request,pk):
    student=Student.objects.get(sid=pk)
    student.delete()
    return redirect("viewStudent")
