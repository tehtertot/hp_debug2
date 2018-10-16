from django.db import models
from apps.ollivanders.models import Wand

class StudentManager(models.Manager):
    def my_validator(self, data_from_form):
        errors = {}
        if len(data_from_form["first_name"]) < 2:
            errors["firstname"] = "First name must be at least 2 characters"
        if len(data_from_form["last_name"]) < 2:
            errors["lastname"] = "Last name must be at least 2 characters"
        return errors

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    wand = models.OneToOneField(Wand, related_name="owner")
    objects = StudentManager
    def full_name(self):
        return f"{self.first_name} {self.last_name}"