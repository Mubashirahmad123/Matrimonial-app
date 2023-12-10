# from collections.abc import Iterable
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# from django.contrib.auth.models import AbstractUser  # Import AbstractUser
from django.contrib.auth.models import User





fs = FileSystemStorage(location=settings.MEDIA_ROOT)

# Create your models here.


class Religion(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    



class Sect(models.Model):
    name = models.CharField(max_length=100)
    religion=models.ForeignKey(Religion,on_delete=models.CASCADE, related_name='sects')
    def __str__(self):
        return self.name    
    



class Caste(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name    

class Hobby(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Hobbies'
    def __str__(self):
        return self.name


class FatherProfile(models.Model):
    name = models.CharField(max_length=100)
    occupation=models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.name








class profile(models.Model):
    name = models.CharField(max_length=100)
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female')
    ]
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)

    profile_pic=models.ImageField(null=True, blank=True)
    email = models.EmailField(max_length=200,unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES)
    occupation=models.CharField(max_length=100,null=True, blank=True)
    date_of_birth=models.DateField(null=True)
    is_married=models.BooleanField(default=False)
    religion=models.ForeignKey(Religion,on_delete=models.CASCADE, related_name='profiles', null=True)
    sect=models.ForeignKey(Sect,on_delete=models.CASCADE, related_name='profiles', null=True)

    caste=models.ForeignKey(Caste,on_delete=models.CASCADE, related_name='profiles', null=True)
    hobbies=models.ManyToManyField(Hobby, related_name='profiles')
    father=models.OneToOneField(FatherProfile, on_delete=models.CASCADE, related_name='dependant', null=True)

    def save(self, *args, **kwargs):
        print(f"Data Updated for {self.name}")
        super().save(*args, **kwargs)
        


    def __str__(self):
        return self.name


# class CustomUser(AbstractUser):
#     # GENDER_CHOICES = [
#     #     ('M', 'Male'),
#     #     ('F', 'Female')
#     # ]

#     # gender = models.CharField(max_length=1,choices=GENDER_CHOICES)



    # is_email_verified = models.BooleanField(default=False)

    # email_verification_token = models.CharField(max_length=200, blank=True, null=True)



class Message(models.Model):
    sender = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='received_messages')
    
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} - {self.subject}"