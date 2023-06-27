from django.db import models

# Create your models here.

class departmentmodel(models.Model):
    dept_name=models.CharField(max_length=20)
    dept_dis=models.TextField()

    def __str__(self):
        return self.dept_name

class doctorsmodel(models.Model):
    doc_img=models.ImageField(upload_to="Hospitalapp/static")
    doc_name=models.CharField(max_length=25)
    dept_name=models.ForeignKey(departmentmodel,on_delete=models.CASCADE)
    doc_spec=models.CharField(max_length=200)

    def __str__(self):
        return '' + self.doc_name + '-(' + self.doc_spec + ')'

class bookingmodel(models.Model):
    p_name=models.CharField(max_length=20)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.CharField(max_length=20)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)