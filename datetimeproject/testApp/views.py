from django.shortcuts import render
import datetime
from .models import Student
# Create your views here.
def home(request):
    presentdatetime = datetime.datetime.now()
    students = Student.objects.all()
    context = {
        'presentdatetime' : presentdatetime,
        'students' : students,
    }
    return render(request, 'home.html',context)