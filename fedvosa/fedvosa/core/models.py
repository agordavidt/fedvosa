from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

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
        ('SET 2021', 'SET 2021'), ('SET 2020', 'SET 2020'),  ('SET 2019', 'SET 2019'), ('SET 2018', 'SET 2018'),
         ('SET 2017', 'SET 2017'), ('SET 2016', 'SET 2016'),  ('SET 2015', 'SET 2015'), ('SET 2014', 'SET 2014'),
          ('SET 2013', 'SET 2013'), ('SET 2012', 'SET 2012'),  ('SET 2011', 'SET 2011'), ('SET 2010', 'SET 2010'),
         ('SET 2009', 'SET 2009'), ('SET 2008', 'SET 2008'),  ('SET 2007', 'SET 2007'), ('SET 2006', 'SET 2006'),
          ('SET 2005', 'SET 2005'), ('SET 2004', 'SET 2004'),  ('SET 2003', 'SET 2003'), ('SET 2002', 'SET 2002'),
          ('SET 2001', 'SET 2001')
    ), blank=True)
    house = models.CharField(max_length=50, choices = (
        ('Mande House', 'Mande House'), ('Abugh House', 'Abugh House'),
        ('Kuma House', 'Kuma House'), ('Pine House', 'Pine House')
    ), blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    relationship = models.CharField(max_length=50, choices = (
        ('single', 'Single'), ('married', 'Married')
    ), blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user