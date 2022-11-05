
from django.contrib import admin
from django.urls import path
from todoapp.views import AddTodoItem
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', AddTodoItem.as_view())
]
