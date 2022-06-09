from django.db import models

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=100)
    message=models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return self.name