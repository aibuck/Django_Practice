from django.urls import path
from . import views
# 127.0.0.1:8000/myapp/

urlpatterns = [
    path(route="", view=views.index),
    path(route="create", view=views.add_todo),
    path(route="delete/<int:todo_id>", view=views.delete_todo),
]