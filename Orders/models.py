from django.db import models

# Create your models here.
class OrdersTB(models.Model):
    name=models.CharField(max_length=50,null=False)
    quantity=models.IntegerField(null=False)
    price=models.IntegerField(null=False)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
    
    
