from django.db import models

# User model
class user(models.Model):  # Capitalized class name for consistency with Django conventions
    username = models.CharField(max_length=250, primary_key=True)  # Consider using UUID for scalability
    email = models.EmailField(max_length=250)  # Changed to EmailField for email validation
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username


# Standard model
class Standard(models.Model):
    standard = models.CharField(max_length=250)
    grade = models.CharField(max_length=250)
    strand = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.grade} - {self.strand}"


# LessonPlan model
class LessonPlan(models.Model):
    lesson_plan_id = models.AutoField(primary_key=True)
    standards = models.ManyToManyField(Standard)
    objectives = models.TextField()
    materials = models.TextField()
    links = models.URLField(max_length=250)  # URLField is already max 200 by default
    assessment = models.TextField()
    curricular_barriers = models.TextField()
    options_for_engagement = models.TextField()
    options_for_representation = models.TextField()
    options_for_action_and_expression = models.TextField()
    iep_goals = models.TextField()
    scripting_of_lesson = models.TextField()

    def __str__(self):
        return f"Lesson Plan {self.lesson_plan_id}"


# Lesson model
class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField()
    suggested_format = models.CharField(max_length=250)
    notes = models.TextField()

    def __str__(self):
        return self.title
