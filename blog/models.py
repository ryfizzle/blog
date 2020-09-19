from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length = 20)
    title = models.CharField(max_length = 40)
    body = models.TextField()
    image = models.ImageField(upload_to = 'blog-images')
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)
    published = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    class Meta:
        ordering = ('-date_created',)