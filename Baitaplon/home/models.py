from django.db import models
from django.core.exceptions import ValidationError

class DictionaryEntry(models.Model):
    id = models.AutoField(primary_key=True)  
    english = models.CharField(max_length=100, unique=True)
    vietnam = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    pronounce = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id}: {self.english}"
    
    def validate_unique(self, exclude=None):
        # Kiểm tra tính duy nhất của trường 'english'
        if DictionaryEntry.objects.filter(english=self.english).exclude(pk=self.pk).exists():
            raise ValidationError('Từ tiếng Anh đã tồn tại.')

    class Meta:
        verbose_name_plural = 'Dictionary Entries'

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)  
    vnconversation = models.CharField(max_length=500)
    enconversation = models.CharField(max_length=500)
     
    def __str__(self):
        return f"{self.id}: {self.enconversation}"