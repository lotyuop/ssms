from django.db import models

SEX_CHOICES = (
    ('1', 'Male.'),
    ('2', 'Female.'),

)
# Create your models here.
class Appstudent(models.Model):
    appno=models.CharField(max_length=12,unique=True)
    surname=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    other_name=models.CharField(max_length=50, null=True)
    sex=models.IntegerField(choices=SEX_CHOICES)
    dob=models.DateField("Date of Birth")
    campus=models.ForeignKey('school.campus',on_delete=models.CASCADE,to_field='')
    sclass=models.ForeignKey('school.Schoolclass', on_delete=models.CASCADE)
    phone=models.CharField(max_length=16)
    home_address=models.TextField()
    raddress=models.TextField("residential Address")
    country=models.CharField(max_length=40,default='Nigeria')
    state=models.ForeignKey('school.State', on_delete=models.CASCADE)
    lga=models.ForeignKey('school.Lga', on_delete=models.CASCADE)
    parent_name=models.CharField(max_length=120)
    parent_phone=models.CharField(max_length=16)
    parent_phone2 = models.CharField(max_length=16)
    parent_email = models.EmailField(max_length=40)
    parent_occupation = models.CharField(max_length=120)
    blood_group=models.ForeignKey('school.Bloodgroup', on_delete=models.CASCADE)
    health_condition=models.TextField()


    def __str__(self):
        return self.top_name

class Admission(models.Model):
    applicant=models.ForeignKey(Appstudent, on_delete=models.CASCADE,to_field='appno')
    exam_date=models.DateField()
    result=models.IntegerField()
    admission_status=models.IntegerField()

    def __str__(self):
        return self.applicant
