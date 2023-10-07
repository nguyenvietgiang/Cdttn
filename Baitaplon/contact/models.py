from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)  
    subject = models.CharField(max_length=255) 
    message = models.TextField()  

    def __str__(self):
        return self.name  

