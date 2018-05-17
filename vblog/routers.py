from rest_framework import routers
from todo_list.viewsets import TodoListViewSet

router = routers.DefaultRouter()

router.register(r'todolist',TodoListViewSet)