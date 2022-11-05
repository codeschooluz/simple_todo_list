from django.db import models

# Create your models here.
class TodoItem(models.Model):
    """
    A todo item
    """
    title = models.CharField(max_length=255)
    task = models.TextField()
    status = models.BooleanField(default=False)
    description = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'task': self.task,
            'status': self.status,
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return self.title