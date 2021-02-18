from django.db import models
from django.contrib.auth.models import User

 

# Create your models here.
 
class Profile(models.Model):
    first_name=models.CharField(max_length=200,null=True)
    last_name=models.CharField(max_length=200,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=200,blank=True)
    age_group=models.IntegerField(null=True)
    profile_pic=models.ImageField(default="avatar.jpg",null=True)
    
   

    def __str__(self):
        return self.user.username
    def get_all_authors_posts(self):
        return self.post_set.all()