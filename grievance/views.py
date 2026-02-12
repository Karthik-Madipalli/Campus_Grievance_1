from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)

        Student.objects.create(
            roll=data["roll"],
            name=data["name"],
            mail=data["mail"],
            pswd=data["pswd"],
            mobile=""
        )

        return JsonResponse({"success":True})


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)

        exists = Student.objects.filter(
            roll=data["roll"],
            pswd=data["pswd"]
        ).exists()

        return JsonResponse({"success":exists})
# --- VIEWS TO RENDER HTML PAGES ---

def index(request):
    return render(request, 'grievance/index.html')

def login_page(request):
    return render(request, 'grievance/login.html')

def signin_page(request):
    return render(request, 'grievance/signin.html')

def student_dashboard(request):
    return render(request, 'grievance/student.html')

def staff_dashboard(request):
    return render(request, 'grievance/staff.html')

def complaint_page(request):
    return render(request, 'grievance/complaint.html')