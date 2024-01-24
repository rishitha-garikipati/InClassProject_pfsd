from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UsersForm
# Create your views here.
def home(request):
    return  render(request,"base.html")

def signup(request):
    if request.method == "POST":
        userform = UsersForm(request)
    else:
        userform = UsersForm()
    return render(request,"signup.html",{"form":userform})