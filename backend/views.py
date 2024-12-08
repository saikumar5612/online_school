from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import user, Standard, LessonPlan, Lesson  # Ensure proper imports
import json

def home(request):
    return HttpResponse("Welcome")

def test(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        emailid = request.POST.get("email", "")
        password = request.POST.get("password", "")

        userone = user(username=username, email=emailid, password=password)
        userone.save()
        return HttpResponse("User is created")
    return HttpResponse("GET request")

@csrf_exempt
def lesson(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            title = data.get("title", "")
            description = data.get("description", "")
            link = data.get("link", "")
            suggested_format = data.get("suggested_format", "")
            notes = data.get("notes", "")

            if not all([title, description, link, suggested_format, notes]):
                return HttpResponse("Error: Missing required fields.", status=400)

            lessonone = Lesson(
                title=title,
                description=description,
                link=link,
                suggested_format=suggested_format,
                notes=notes,
            )
            lessonone.save()
            return HttpResponse("Lesson added successfully!")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data.", status=400)
    return HttpResponse("GET request not supported.")

@csrf_exempt
def standard(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            standard = data.get("standard", "")
            grade = data.get("grade", "")
            strand = data.get("strand", "")

            if not all([standard, grade, strand]):
                return HttpResponse("Error: Missing required fields.", status=400)

            standards = Standard(
                standard=standard,
                grade=grade,
                strand=strand,
            )
            standards.save()
            return HttpResponse("Standard added successfully!")
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data.", status=400)
    return HttpResponse("GET request not supported.")
