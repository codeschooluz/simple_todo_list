from django.db import models

# Create your models here.
class TodoItem(models.Model):
    """
    A todo item
    """
    title = models.CharField(max_length=255)
    task = models.TextField()
    status = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title