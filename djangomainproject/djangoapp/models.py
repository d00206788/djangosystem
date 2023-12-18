from django.db import models

# Create your models here.

class Usersinfo(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
    
class Breed(models.Model):
    STATUS = (
        ('Alive', 'Alive'),
        ('Deceased', 'Deceased'),
    )
    userinfo = models.ForeignKey(Usersinfo, null=True, on_delete=models.SET_NULL) 
    name = models.CharField(max_length=200, null=True)
    breedname = models.CharField(max_length=200, null=True)
    age = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    # creating a one to many relationship, for userinfo to point to User table. Adding on_delete, which means if a user id deleted, clears user info but the dog info remains. Relates to tag also
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.name




