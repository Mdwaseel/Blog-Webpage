from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Lifestyle', 'Lifestyle'),
        ('Finance', 'Finance'),
        ('Education', 'Education'),
        ('Food_Cooking', 'Food and Cooking'),
        ('Business_Entrepreneurship', 'Business and Entrepreneurship'),
        ('Book_Movie_Reviews', 'Book and Movie Reviews'),
        ('Parenting', 'Parenting'),
        ('Science_Nature', 'Science and Nature'),
        ('Art_Creativity', 'Art and Creativity'),
        # Add more choices as needed
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    date_uploaded = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Lifestyle')

    class Meta:
        ordering = ('-date_uploaded',)

    def __str__(self):
        return self.title



class Profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

