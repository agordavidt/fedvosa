from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=12)
    gradset = models.CharField(max_length=50, choices = (
        ('0', 'SET 2021'), ('1', 'SET 2020'),  ('2', 'SET 2019'), ('3', 'SET 2018'),
         ('4', 'SET 2017'), ('5', 'SET 2016'),  ('6', 'SET 2015'), ('7', 'SET 2014'),
          ('8', 'SET 2013'), ('9', 'SET 2012'),  ('10', 'SET 2011'), ('11', 'SET 2010'),
         ('12', 'SET 2009'), ('13', 'SET 2008'),  ('14', 'SET 2007'), ('15', 'SET 2006'),
          ('16', 'SET 2005'), ('17', 'SET 2004'),  ('18', 'SET 2003'), ('19', 'SET 2002'),
          ('20', 'SET 2001')
    ), blank=True)
    house = models.CharField(max_length=50, choices = (
        ('mande', 'Mande House'), ('abugh', 'Abu House'),
        ('kuma', 'Kuma House'), ('pine', 'Pine House')
    ), blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=50, choices = (
        ('single', 'Single'), ('married', 'Married')
    ), blank=True)

    def __str__(self):
        return self.user.username