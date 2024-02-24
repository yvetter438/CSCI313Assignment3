from django.urls import path
from . import views
from .views import course_detail

urlpatterns = [
    path("", views.index, name = ""),
    path("course/<int:course_id>/", course_detail, name="course_detail")
]