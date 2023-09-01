from django.db import models

class DictionaryEntry(models.Model):
    id = models.AutoField(primary_key=True)  
    english = models.CharField(max_length=100)
    vietnam = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    pronounce = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.english}"
