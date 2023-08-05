"""JobPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from job_portal import views
from django.conf import settings
from django.conf.urls.static import static
import job_portal

urlpatterns = [
    path('', views.home),
    path('sampleresume/', views.sampleresume),
    path('companies/', views.companies),
    path('aboutus/', views.aboutus),
    path('signinstudent/', views.signinstudent),
    path('signinrecruiter/', views.signinrecruiter),
    path('signupstudent/', views.signupstudent),
    path('signuprecruiter/', views.signuprecruiter),
    path('register/', views.register),
    path('registerStudent/', views.registerStudent),
    path('loginRecruiter/', views.loginRecruiter),
    path('loginStudent/', views.loginStudent),
    path('Logout/', views.Logout),
    path('recruiter_home/', views.recruiter_home, name="recruiter_home"),
    path('student_home/', views.student_home, name="student_home"),
    path('latest_jobs/', views.latest_jobs),
    path('student_latestjobs/', views.student_latestjobs, name="student_latestjobs"),
    path('add_job/', views.add_job),
    path('job_list/', views.job_list),
    path('job_detail/<int:pid>', views.job_detail, name="job_detail"),
    path('applyforjob/<int:pid>', views.applyforjob, name="applyforjob"),
    path('applied_candidates/', views.applied_candidates, name="applied_candidates"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
