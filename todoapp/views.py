from django.shortcuts import render
from django.views import View
from .models import TodoItem
from django.http import JsonResponse
import json

# Create view for the add todo item
class AddTodoItem(View):
    def post(self, request):
        """
        Add a todo item
        args:
            request: the request object
        returns:
            JsonResponse: the response object
        """
        # Get the data from the request
        title = request.POST.get('title')
        task = request.POST.get('task')
        # Create the todo item
        todo_item = TodoItem(title=title, task=task)
        todo_item.save()                  
        return JsonResponse({'message': 'Todo item created successfully'})
