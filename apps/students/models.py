from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

from apps.corecode.models import StudentClass, Subject


class Student(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]
  
  FILIEREBAC = [
      ('sciencesMaths', 'sciencesMaths'),
      ('sciencesPhysique', 'sciencesPhysique'),
      ('svt', 'svt')
  ]

  
  

  current_status        = models.CharField(max_length=10, choices=STATUS, default='active')
  registration_number   = models.CharField(max_length=200, unique=True)
  surname               = models.CharField(max_length=200)
  firstname             = models.CharField(max_length=200)
  gender                = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth         = models.DateField(default=timezone.now)
  filiere_bac           = models.CharField(max_length=20, choices=FILIEREBAC, default='sciences maths')
  note_bac              = models.CharField(max_length=200, blank=True)
  current_class         = models.ForeignKey(StudentClass, on_delete=models.SET_NULL, blank=True, null=True)
  date_of_admission     = models.DateField(default=timezone.now)

  mobile_num_regex      = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  parent_mobile_number  = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)

  address               = models.TextField(blank=True)
  others                = models.TextField(blank=True)
  image                 = models.ImageField(blank=True, upload_to='students/images/') 
  bac_scan              = models.ImageField(blank=True, upload_to='students/BacScan/')  
  releve_notes_scan     = models.ImageField(blank=True, upload_to='students/RelveNotesScan/')   

  class Meta:
    ordering = ['surname', 'firstname', 'note_bac']

  def __str__(self):
    return f'{self.surname} {self.firstname} {self.note_bac} ({self.registration_number})'

  def get_absolute_url(self):
    return reverse('student-detail', kwargs={'pk': self.pk})


class StudentBulkUpload(models.Model):
  date_uploaded       = models.DateTimeField(auto_now=True)
  csv_file            = models.FileField(upload_to='students/bulkupload/')

