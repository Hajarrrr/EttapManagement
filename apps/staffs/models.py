from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

from apps.corecode.models import Subject

class Staff(models.Model):
  STATUS = [
      ('active', 'Active'),
      ('inactive', 'Inactive')
  ]

  GENDER = [
      ('male', 'Male'),
      ('female', 'Female')
  ]

  TYPEPOST = [
      ('Enseignant', 'Enseignant'),
      ('Support', 'Support')
  ]

  SUBJECTS = [
      ('FR', 'FR'),
      ('MATH', 'MATH')
  ]

  current_status      = models.CharField(max_length=10, choices=STATUS, default='active')
  surname             = models.CharField(max_length=200)
  firstname           = models.CharField(max_length=200)
  
  gender              = models.CharField(max_length=10, choices=GENDER, default='male')
  date_of_birth       = models.DateField(default=timezone.now)
  date_of_admission   = models.DateField(default=timezone.now)


  type_post           = models.CharField(max_length=10, choices=TYPEPOST, default='Enseignant')
  poste               = models.CharField(max_length=200, blank=True)
  # subject             = models.CharField(max_length=10, choices=SUBJECTS, default='MATH')
  subject             = models.ForeignKey(Subject, on_delete=models.CASCADE)
  subject_1            = models.ForeignKey(Subject, related_name='one', on_delete=models.CASCADE)
  subject_2            = models.ForeignKey(Subject, related_name='two', on_delete=models.CASCADE)
  

  mobile_num_regex    = RegexValidator(regex="^[0-9]{10,15}$", message="Entered mobile number isn't in a right format!")
  mobile_number       = models.CharField(validators=[mobile_num_regex], max_length=13, blank=True)
  
  address             = models.TextField(blank=True)
  others              = models.TextField(blank=True)

  def __str__(self):
    return f'{self.surname} {self.firstname} '

  def get_absolute_url(self):
    return reverse('staff-detail', kwargs={'pk': self.pk})
