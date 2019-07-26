from django.db import models

# Create your models here.


class category(models.Model):
    brand = models.CharField(max_length=20)
    item = models.CharField(max_length=20)
    originalprice = models.IntegerField(null=True)
    
    file = models.FileField(null=True)

    def __str__(self):
        return (str(self.brand)+''+str(self.item))
