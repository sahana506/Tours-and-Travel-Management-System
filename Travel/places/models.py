from django.db import models


class Sources(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Dest(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    

class Details(models.Model):
    name = models.CharField( max_length=100)
    phno = models.CharField( max_length=10)
    email = models.CharField( max_length=100)
    age = models.IntegerField()
    source =models.ForeignKey(Sources,on_delete=models.CASCADE)
    dest =models.ForeignKey(Dest,on_delete=models.CASCADE)
    departure = models.CharField(max_length=50,default='none')
    return_date = models.CharField(max_length=50,default='none')
    
   # leaving_date = models.CharField(max_length=50)
    #arriving_date = models.DateField(max_length=50)
    

    def __str__(self):
        return self.name

class Catalog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary

class Idnum(models.Model):
    idno = models.CharField(max_length=10)

    def __str__(self):
        return self.idno

