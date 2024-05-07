from django.contrib import admin
# from .models import Item

# Register your models here.
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#   list_display = ['name']


from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin) :
    pass