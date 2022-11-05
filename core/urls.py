
from django.contrib import admin
from django.urls import path
from todoapp.views import AddTodoItem, GetAllTodoItems
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', AddTodoItem.as_view()),
    path('get/', GetAllTodoItems.as_view()),

]
