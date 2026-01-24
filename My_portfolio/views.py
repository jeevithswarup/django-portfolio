from django.shortcuts import render,redirect,get_object_or_404
from .models  import *


def Home(request):
     projects = Projects.objects.all()   
     skills =Skills.objects.all()
     intro=Intro.objects.first()

     try:
        urls = SocialMediaLink.objects.first()
     except:
        urls = None
    #  urls=SocialMediaLink.objects.first() or SocialMediaLink()
     context={
         'projects': projects,
          'skills': skills,
          'intro' : intro,
          'urls':urls,
      }
     return render(request,'My_portfolio/home.html',context)        
def contact(request):
     if request.method=='POST':
         visitor_name=request.POST.get("name")
         visitor_email=request.POST.get("email")
         visitor_message=request.POST.get("message")

         Contact.objects.create(
             visitor_name=visitor_name,
             visitor_email=visitor_email,
             visitor_message=visitor_message
             
         )
     return  redirect("/")
def Project_details(request,id):
    intro=Intro.objects.first()
    project=Projects.objects.all()
    projects = Projects.objects.prefetch_related('features')

    project=get_object_or_404(project,id=id)
    return render(request,'My_portfolio/Project.html',{"project": project,"intro":intro})

def Academics(request):
    academics=AcademicQualification.objects.all()
    certificates=Certificates.objects.all()
    semester=Semester.objects.all()
    intro=Intro.objects.first()

    return render(request,'My_portfolio/academics.html',{
        'academics':academics,
        'certificates':certificates,
        'semester':semester,
        'intro':intro,
    })   
