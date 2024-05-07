# from django.shortcuts import render, redirect
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView
# from django.views.generic.edit import UpdateView
# from django.urls import reverse_lazy
# from myapp.models import Item

# # Create your views here.
# def index(request):

#   item_qs = Item.objects.all()

#   return render(
#     request=request,
#     template_name='myapp/index.html',
#     context={
#       'item_qs' : item_qs
#     }
#   )


# class ItemList(ListView):
#   model = Item
#   context_object_name = 'items'

# class ItemDetail(DetailView):
#   model = Item
#   context_object_name = 'item'
#   template_name = 'base'

# class ItemCreate(CreateView):
#   model = Item
#   fields = '__all__'
#   success_url = reverse_lazy('items')

# class ItemUpdate(UpdateView):
#   model = Item
#   fields = '__all__'
#   success_url = reverse_lazy('items')





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

