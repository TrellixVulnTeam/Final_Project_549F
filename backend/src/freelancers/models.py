from django.db import models

# Create your models here.
class freelancer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.id
