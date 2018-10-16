from django.db import models

class Wand(models.Model):
    core = models.CharField(max_length=45)
    length = models.FloatField()
    wood = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.length}\" {self.core} {self.wood}"