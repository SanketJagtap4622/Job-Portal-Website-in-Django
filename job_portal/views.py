# Create your views here.

from distutils.log import error
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import * 
from datetime import date

def home(request):
    # return HttpResponse("Welcome to Online JobPortal")
    return render(request, 'job_portal/index.html')

def sampleresume(request):
    return render(request, 'job_portal/sampleresume.html')

def companies(request):
    return render(request, 'job_portal/companies.html')

def aboutus(request):
    return render(request, 'job_portal/aboutus.html')

def signinstudent(request):
    return render(request, 'job_portal/signin student.html')
    
def signinrecruiter(request):
    return render(request, 'job_portal/signin recruiter.html')

def signupstudent(request):
    return render(request, 'job_portal/signup student.html')

def signuprecruiter(request):
    return render(request, 'job_portal/signup recruiter.html')

# def loginStudent(request):
#     if request.method == 'POST':
#         #Get the post parameters
#         username = request.POST['username']
#         password = request.POST['password']

#         adminuser = authenticate(username = username, password = password )

#         if adminuser is not None:
#             login(request,adminuser)
#             messages.success(request, 'Successfully Logged In')
#             return redirect('/')
            
#         else:
#             # messages.error(request, "Invalid Credentials, Please try again!!")
#             return HttpResponse('404 - Not Found')
#     return HttpResponse('404-Not Found')

# def loginStudent(request):
#     # error=""
#     if request.method == 'POST':
#         #Get the post parameters
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username = username, password = password )
#         user1 = StudenttUser.objects.get(user=user)
#         if user is not None:
#             if user1.type == "student":
#                 login(request, user)
#                 messages.success(request, 'Successfully Logged In')
#                 return redirect('/student_home')
#                 # error="no"
#             # else:
#             #     messages.alert(request, 'Something went wrong, Please try again')
#             #     return redirect('job_portal/signin student.html')
#                 # error="yes"
#         else:
#             return HttpResponse('404 - Not Found')
#     return HttpResponse('404-Not Found') 

def student_home(request):
    if not request.user.is_authenticated:
        return redirect('/signinstudent/')
    user = request.user
    student = StudenttUser.objects.get(user=user)
    d = {'student':student}
    return render(request, 'job_portal/student_home.html', d)

def loginStudent(request):
    error=""
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password )
        if user:
            try:
                user1 = StudenttUser.objects.get(user=user)
                if user1.type == "student":
                    login(request, user)
                    error="no"
                else:
                    error="yes"
            except:
                    # pass
                    error="yes"
        else:
            error="yes"
    d={"error":error}        
    # return redirect('/', d)
    return render(request, 'job_portal/signin student.html', d)

# def registerStudent(request):
#     if request.method == 'POST':
#         #Get the post parameters
#         lastName = request.POST['lastName']
#         firstName = request.POST['firstName']
#         username = request.POST['username']
#         email = request.POST['email']
#         password= request.POST['password']
#         cpassword= request.POST['cpassword']

#         #Check for errorinput

#         if password != cpassword:
#             # messages.error(request, "Passwords do not match!!")
#             return redirect('/')

#         if not username.isalnum():
#             # messages.error(request, "Username should contain only letters and numbers!!")
#             return redirect('/')

#         #Create User
#         myuser = User.objects.create_user(username, email, password)
#         myuser.first_name = firstName
#         myuser.last_name = lastName
#         myuser.save()
#         messages.success(request, "Your Student account was created successfully!!")
#         return redirect('/signinstudent/')        
#     else:
#         return HttpResponse('404 - Not Found')

def registerStudent(request):
    # error=""
    if request.method == 'POST':
        #Get the post parameters
        lastName = request.POST['lastName']
        firstName = request.POST['firstName']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password= request.POST['password']
        cpassword= request.POST['cpassword']

        #Create User
        user=User.objects.create_user(username=username, password=password)   
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        StudenttUser.objects.create(user=user, email=email, mobile=mobile, type='student')
        return redirect('/signinstudent/')
    else:
        return HttpResponse('404 - Not Found')
        
# def studentLogout(request):
#     logout(request)
#     messages.success(request, 'Successfully Logged Out')
#     return redirect('/')

# def register(request):
#     if request.method == 'POST':
#         #Get the post parameters
#         lastName = request.POST['lastName']
#         firstName = request.POST['firstName']
#         username = request.POST['username']
#         email = request.POST['email']
#         password= request.POST['password']
#         cpassword= request.POST['cpassword']

#         #Check for errorinput

#         if password != cpassword:
#             # messages.error(request, "Passwords do not match!!")
#             return redirect('/')

#         if not username.isalnum():
#             # messages.error(request, "Username should contain only letters and numbers!!")
#             return redirect('/')

#         #Create User
#         myuser = User.objects.create_user(username, email, password)
#         myuser.first_name = firstName
#         myuser.last_name = lastName
#         myuser.save()
#         # messages.success(request, "Your Recruiter account was created successfully!!")
#         return redirect('/signinrecruiter/')
        
#     else:
#         return HttpResponse('404 - Not Found')

def register(request):
    # error=""
    if request.method == 'POST':
        #Get the post parameters
        lastName = request.POST['lastName']
        firstName = request.POST['firstName']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password= request.POST['password']
        cpassword= request.POST['cpassword']

        #Create User
        user=User.objects.create_user(username=username, password=password)   
        user.first_name = firstName
        user.last_name = lastName
        user.save()
        Recruiter.objects.create(user=user, email=email, mobile=mobile, type='recruiter')
        return redirect('/signinrecruiter/')
    else:
        return HttpResponse('404 - Not Found')
    
def loginRecruiter(request):
    error=""
    if request.method == 'POST':
        #Get the post parameters
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password )
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == "recruiter":
                    login(request, user)
                    error="no"
                else:
                    error="yes"
            except:
                    # pass
                    error="yes"
        else:
            error="yes"
    d={"error":error}        
    # return redirect('/', d)
    return render(request, 'job_portal/signin recruiter.html', d)

# def loginRecruiter(request):
#     # error=""
#     if request.method == 'POST':
#         #Get the post parameters
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username = username, password = password )
#         user1 = Recruiter.objects.get(user=user)
#         if user is not None:
#             if user1.type == "recruiter":
#                 login(request, user)
#                 # messages.success(request, 'Successfully Logged In')
#                 return redirect('/recruiter_home/')
#                 # error="no"
#             # else:
#                 # error="yes"
#         else:
#             return HttpResponse('404 - Not Found')
#     return HttpResponse('404-Not Found')

# def loginRecruiter(request):
#     if request.method == 'POST':
#         #Get the post parameters
#         username = request.POST['username']
#         password = request.POST['password']

#         adminuser = authenticate(username = username, password = password )

#         if adminuser is not None:
#             login(request,adminuser)
#             # messages.success(request, 'Successfully Logged In')
#             return redirect('/recruiter_home/')
            
#         else:
#             # messages.error(request, "Invalid Credentials, Please try again!!")
#             return HttpResponse('404 - Not Found')
#     return HttpResponse('404-Not Found')

def Logout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')

def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('/signinrecruiter/')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    d = {'recruiter':recruiter}
    return render(request, 'job_portal/recruiter_home.html', d)

def add_job(request):
    if not request.user.is_authenticated:
        return redirect('loginRecruiter')
    # error=""
    if request.method == 'POST':
        #Get the post parameters
        jobtitle = request.POST['jobtitle']
        description = request.POST['description']
        company_name = request.POST['company_name']
        location = request.POST['location']
        skills= request.POST['skills']
        salary= request.POST['salary']
        start_date= request.POST['start_date']
        end_date= request.POST['end_date']
        creation_date = date.today()
        user = request.user
        recruiter = Recruiter.objects.get(user=user)
        try:
            Job.objects.create( recruiter=recruiter, 
                                title=jobtitle, 
                                description=description, 
                                company_name=company_name, 
                                location=location, 
                                skills=skills, 
                                salary=salary, 
                                start_date=start_date, 
                                end_date=end_date, 
                                creation_date=creation_date)
            messages.success(request, 'Successfully Job has been posted')            
            # error="No"
        except:
            pass
            # error="Yes"
    # d={error:error}
    return render(request, 'job_portal/add_job.html')

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('loginRecruiter')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    job = Job.objects.filter(recruiter=recruiter)
    d = {'job':job}
    return render(request, 'job_portal/job_list.html', d)

def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job':job}
    return render(request, 'job_portal/latest_jobs.html', d)

def student_latestjobs(request):
    job = Job.objects.all().order_by('-start_date')
    user = request.user
    student = StudenttUser.objects.get(user=user)
    data = Apply.objects.filter(student=student)
    li=[]
    for i in data:
        li.append(i.job.id)
    d = {'job':job, 'li':li}
    return render(request, 'job_portal/student_latestjobs.html', d)

def job_detail(request,pid):
    job = Job.objects.get(id=pid)
    d = {'job':job}
    return render(request, 'job_portal/job_detail.html', d)

def applyforjob(request,pid):
    if not request.user.is_authenticated:
        return redirect('/signinstudent/')
    error=""
    user = request.user
    student = StudenttUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    if job.end_date < date1:
        # messages.success(request, 'Application lines are closed')
        # return redirect('/student_latestjobs')
        error="close"
    elif job.start_date > date1:
        # messages.success(request, 'Application lines are not opened yet')
        # return redirect('/student_latestjobs')
        error="notopen"
    else:
        if request.method == 'POST':
            r = request.FILES['resume']
            Apply.objects.create(job=job, student=student, resume=r, applydate=date.today())
            # messages.success(request, 'Job Application submitted Successfully')
            # return redirect('/student_latestjobs')
            error="done"
    d = {'error':error}
    return render(request, 'job_portal/applyforjob.html', d)

def applied_candidates(request):
    if not request.user.is_authenticated:
        return redirect('loginRecruiter')

    data = Apply.objects.all()   
    d = {"data":data}        
    return render(request, 'job_portal/applied_candidates.html', d)