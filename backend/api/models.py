from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    full_name = models.CharField(max_length=150)
    ref_name = models.CharField(max_length=20)
    prof_pic = models.ImageField(upload_to="Profile_Pictures/", default="Profile_Pictures/defaultUser.jpg", blank=True)
    bio = models.TextField(null=True)
    skills = models.TextField()
    github = models.CharField(max_length=150, null=True)
    linkedin = models.CharField(max_length=150, null=True) 
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Member")