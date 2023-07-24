from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OurInformation(models.Model):
    address = models.CharField(max_length=1000)
    address_description = models.CharField(max_length=510)
    tell = models.IntegerField()
    tell_description = models.CharField(max_length=510)
    email = models.EmailField()
    email_description = models.CharField(max_length=510)

    def __str__(self):
        return f'addres : {self.address[:50]} & tell {self.tell}'