from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 30)
    contact = models.CharField(max_length=10)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} Object'
    
    class Meta:
        db_table = 'Contact'

