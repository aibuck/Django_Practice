from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from django.shortcuts import redirect

def index(request) :

    todos = Todo.objects.all()

    return render(
        request, 
        "index.html",
        {
            "todos" : todos
        }
    )

def add_todo(request) :

    if request.method == "POST" :
        todo = Todo(
            content=request.POST.get("content"),
            completed=False
            )
        todo.save()
    
    return redirect(index)

def delete_todo(request, todo_id) :

    if request.method == "POST" :
        todo = get_object_or_404(Todo, id=todo_id)
        todo.delete()

    return redirect(index)