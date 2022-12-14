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

# Create view for getting all todo items
class GetAllTodoItems(View):
    def get(self, request):
        """
        Get all todo items
        args:
            request: the request object
        returns:
            JsonResponse: the response object
        """
        # Get all todo items
        todo_items = TodoItem.objects.all()
        
        # Convert todo items to json
        todo_items_json = [todo_item.to_json() for todo_item in todo_items]
        return JsonResponse({'todo_items': todo_items_json})

# Create view for removing a todo item
class RemoveTodoItem(View):
    def get(self, request, id):
        """
        Remove a todo item
        args:
            request: the request object
            id: the todo item id
        returns:
            JsonResponse: the response object
        """
        # Get the todo item
        todo_item = TodoItem.objects.get(id=id)
        # Delete the todo item
        todo_item.delete()
        return JsonResponse({'todo': todo_item.to_json()})

# Create view for updating a todo item
class UpdateTodoItem(View):
    def post(self, request, id):
        """
        Update a todo item
        args:
            request: the request object
            id: the todo item id
        returns:
            JsonResponse: the response object
        """
        # Get the todo item
        todo_item = TodoItem.objects.get(id=id)
        # Get the data from the request
        title = request.POST.get('title')
        task = request.POST.get('task')
        status = request.POST.get('status')
        description = request.POST.get('description')
        # Update the todo item
        todo_item.title = title
        todo_item.task = task
        todo_item.status = status
        todo_item.description = description
        todo_item.save()
        return JsonResponse({'todo': todo_item.to_json()})