from django.db import models

# Create your models here.
class product(models.Model):
    pbrand = models.CharField(max_length=20)
    pitem = models.CharField(max_length=20, null=True)
    productimg_name =models.CharField(max_length =40, null=True)

    originalprice = models.IntegerField(null=True)
    lowerlimit = models.IntegerField(null=True)
    pub_date = models.DateTimeField('date published')

    user_id = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.pbrand)+''+str(self.pitem)