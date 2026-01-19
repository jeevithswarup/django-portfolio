
from django.db import models
from .storages import ImageStorage, PDFStorage
from cloudinary.models import CloudinaryField



class Projects(models.Model):
    title=models.CharField(max_length=50)
    short_description=models.CharField(max_length=150)
    detialed_description=models.TextField(max_length=1000)
    tech_stack=models.CharField(max_length=300)
    Category=models.CharField(max_length=50,default='Backend Developer')
    status=models.CharField(max_length=50,default='In Progress')
#     image=models.ImageField(upload_to="project_image/",blank=True,null=True)
#     project_pdf = models.FileField(upload_to="project_pdfs/",blank=True,null=True)
   
    image = models.ImageField(
        upload_to="project_image/",
        storage=ImageStorage(),
        blank=True,
        null=True
    )

    project_pdf = models.FileField(
        upload_to="project_pdfs/",
        storage=PDFStorage(),
        blank=True,
        null=True
    )
    github_link=models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    

class Skills(models.Model):
        skill_name=models.CharField(max_length=200)
        icon=models.CharField(max_length=50)
        #skill level later
        def __str__(self):
             return self.skill_name
        

class Contact(models.Model):
    visitor_name=models.CharField(max_length=100)
    visitor_email=models.EmailField()
    visitor_message=models.TextField()    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.visitor_name
    
class Intro(models.Model):
        logo_name=models.CharField(max_length=30)
        profile_name=models.CharField(max_length=50)
        role=models.CharField(max_length=100,default='Full Stack Web-Developer')
        introduction=models.TextField()
     #    profile_img=models.ImageField(upload_to='profile_img/', blank=True, null=True)
        profile_img = models.ImageField(
        upload_to='profile_img/',
        storage=ImageStorage(),
        blank=True,
        null=True
        )
        about_me=models.TextField()
     #    resume_pdf=models.FileField(upload_to='resume_pdf/',blank=True,null=True)
    #     resume_pdf = models.FileField(
    #     upload_to='resume_pdf/',
    #     storage=PDFStorage(),
    #     blank=True,
    #     null=True
    # )
        resume_pdf = CloudinaryField(
        resource_type="image",
        folder="resume_pdf"
    )
        footer_name=models.CharField(max_length=50,blank=True)
        def __str__(self):
               return self.profile_name
        
        def save(self, *args, **kwargs):
         if not self.pk and Intro.objects.exists():
            raise Exception("Only one Intro instance is allowed!")
         return super(Intro, self).save(*args, **kwargs) 
         
class AcademicQualification(models.Model):
     qualification=models.CharField(max_length=50)
     board=models.CharField(max_length=50)
     institute_name=models.CharField(max_length=100)
     percentage=models.DecimalField(
          max_digits=5,
          decimal_places=2
     )
     start_year=models.PositiveIntegerField()
     end_year=models.PositiveIntegerField()
     # result_pdf=models.FileField(upload_to='results/',blank=True,null=True)
     result_pdf = models.FileField(
        upload_to='results/',
        storage=PDFStorage(),
        blank=True,
        null=True
    )

     def __str__(self):
          return self.qualification

class Certificates(models.Model):
     # certificate_pdf=models.FileField(upload_to='certificates/',blank=True,null=True)    
     certificate_pdf = models.FileField(
        upload_to='certificates/',
        storage=PDFStorage(),
        blank=True,
        null=True
    )
     certificate_name=models.CharField(max_length=50)

     def __str__(self):
          return self.certificate_name

class Semester(models.Model):
     qualification = models.ForeignKey(
        AcademicQualification,
        on_delete=models.CASCADE,
        related_name="semesters"
    )
     semester_number=models.PositiveSmallIntegerField()
     # semester_result=models.FileField(upload_to='sem_results/',blank=True,null=True)
     semester_result = models.FileField(
        upload_to='sem_results/',
        storage=PDFStorage(),
        blank=True,
        null=True
    )
     def __str__(self):
         return  f"{self.qualification} - Semester {self.semester_number}"
     
class KeyFeature(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name="features")
    feature_text = models.CharField(max_length=255)

    def __str__(self):
        return self.feature_text     