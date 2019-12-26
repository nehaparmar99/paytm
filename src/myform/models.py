from django.db import models
# Create your models here.
class ContactModel(models.Model):
    name= models.CharField(max_length=120)
    email=models.TextField(blank=True, null=True)
    number= models.DecimalField(decimal_places=0,max_digits=1000)
    workshops=models.TextField(blank=True, null=True)
    def __str__(self):
        return self.name[:50]