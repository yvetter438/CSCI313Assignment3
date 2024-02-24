from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, "index.html", {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, courseID=course_id)
    return render(request, "course_detail.html", {"course": course})