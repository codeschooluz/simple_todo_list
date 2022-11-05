
from django.contrib import admin
from django.urls import path
from todoapp.views import AddTodoItem, GetAllTodoItems,RemoveTodoItem,UpdateTodoItem
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', AddTodoItem.as_view()),
    path('get/', GetAllTodoItems.as_view()),
    path('remove/<int:id>/', RemoveTodoItem.as_view()),
    path('update/<int:id>/', UpdateTodoItem.as_view()),

]
