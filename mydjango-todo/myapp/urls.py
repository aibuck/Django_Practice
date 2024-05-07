# from django.urls import path
# from .views import *
# # from . import views
# # 127.0.0.1:8000/myapp/hello

# urlpatterns = [
#   path('', index),
#   path('item/<int:pk>/', ItemDetail.as_view(), name='item'),
#   path('item-create/', ItemCreate.as_view(), name='item-create'),#addtodo()
#   path('task-update/<int:pk>/', ItemUpdate.as_view(), name='task-update'),
# ]

from django.urls import path
from . import views
# 127.0.0.1:8000/myapp/

urlpatterns = [
    path(route="", view=views.index),
    path(route="create", view=views.add_todo),
    path(route="delete/<int:todo_id>", view=views.delete_todo),
]