from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    # Optional: Link to Django's User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    student_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.student_name} ({self.student_id})"

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ['student_name']
