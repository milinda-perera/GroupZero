from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# model class for Members
class Members(models.Model):
    full_name = models.CharField(max_length=150)
    ref_name = models.CharField(max_length=20)
    prof_pic = models.ImageField(upload_to="Profile_Pictures/", default="Profile_Pictures/defaultUser.jpg", blank=True)
    bio = models.TextField(null=True)
    skills = models.TextField()
    github = models.CharField(max_length=150, null=True)
    linkedin = models.CharField(max_length=150, null=True) 
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Member")

    def __str__(self):
        return self.ref_name


# model class for Projects
class Projects(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    project_pics = models.JSONField(null=True, blank=True)
    cover_pic = models.ImageField(upload_to="Project_cover_Pictures/", null=True, blank=True, default="Project_cover_Pictures/defaultProject.jpg")
    demo_link = models.CharField(max_length=150, null=True)
    category = models.CharField(max_length=150, null=False, default="Web Development")
    def __str__(self):
        return self.title


# model class for reviews
class Reviews(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating
