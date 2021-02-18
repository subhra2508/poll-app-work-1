from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
# Create your models here.
CATAGORIES=( 
    ('movies','movies'),
    ('sports','sports'),
    ('political','political'),
    ('general','general'),
 
)
class Post(models.Model):
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='poll_like',blank=True)
    dislike=models.ManyToManyField(User,related_name='poll_dislike',blank=True)
    catagory=models.CharField(max_length=20,null=True,choices=CATAGORIES)
    author=models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="posts")

    def __str__(self):
        return str(self.content)

class Comment(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField(max_length=200) 
  

    def __str__(self):
        return str(self.pk)
    def get_comment_details(self):
        return str(self.body)