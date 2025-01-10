from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse 

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=30)
    default_image_path = 'web-dev-1.jpg'
    image = models.ImageField(upload_to='assets/media/blog_images', default=default_image_path)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', kwargs={'pk': self.pk})
        return reverse('blog-home')
    
