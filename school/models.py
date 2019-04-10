from django.db import models

# Create your models here.

class State(models.Model):
    state_name=models.CharField(max_length=80)

    def __str__(self):
        return self.state_name

class Lga(models.Model):
    state=models.ForeignKey('state', on_delete=models.CASCADE)
    lga_name=models.CharField(max_length=90)


    def __str__(self):
        return self.lga_name

class SchoolClass(models.Model):
    sclass=models.CharField(max_length=10)
    total_pupil=models.IntegerField()

    def __str__(self):
        return self.sclass

class SubClass(models.Model):
    sclass=models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    subclass=models.CharField(max_length=10)
    num_pupil=models.IntegerField()

    def __str__(self):
        return self.subclass

class Bloodgroup(models.Model):
  bloodg=models.CharField(max_length=1)
  factor=models.CharField(max_length=10)

  def __str__(self):
      return self.bloodg

TYPE_CHOICES=(
    ('private', 'PRIVATE'),
    ('public', 'PUBLIC')
)
class SchoolDit(models.Model):
    name=models.CharField(max_length=150,unique=True)
    short_name=models.CharField(max_length=10,unique=True)
    location=models.TextField
    phone=models.CharField(max_length=18,unique=True)
    email=models.EmailField(unique=True)
    logo=models.TextField()
    school_head=models.CharField(max_length=50)
    school_type=models.CharField(max_length=20)
    hascampus=models.IntegerField()

    def __str__(self):
        return self.name

class Campus(models.Model):
    school=models.ForeignKey(SchoolDit, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    location=models.TextField()
    contact=models.CharField(max_length=16)

    def __str__(self):
        return self.name