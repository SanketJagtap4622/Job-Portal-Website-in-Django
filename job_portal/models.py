from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudenttUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    type = models.CharField(max_length=10, null=True) 
    def _str_(self):
        return self.user.username

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    # company = models.CharField(max_length=150)
    type = models.CharField(max_length=10, null=True) 
    def _str_(self):
        return self.user.username


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    company_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=50)
    salary = models.FloatField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    creation_date = models.DateField()
    
    def _str_(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(StudenttUser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    applydate = models.DateField()
    
    def _str_(self):
        return self.id
