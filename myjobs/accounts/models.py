from django.db import models

# Create your models here.

class employer(models.Model):
    name = models.CharField(max_length=200,null= True)
    phone = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=200,null= True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
class employee(models.Model):
    STATUS =(
        ('Available','Available'),
        ('Not Available','Not Available')
    )
    name = models.CharField(max_length=200,null= True)
    phone = models.CharField(max_length=200,null= True)
    email = models.CharField(max_length=200,null= True)
    address = models.CharField(max_length=200,null= True)
    occupation=models.CharField(max_length=200,null= True)
    experience=models.CharField(max_length=200,null= True)
    date_created = models.DateTimeField(auto_now_add = True)
    status =models.CharField(max_length=200,null= True,choices=STATUS)

    def __str__(self):
        return self.name
    
    class Meta:
        managed= False
        db_table = 'employee'