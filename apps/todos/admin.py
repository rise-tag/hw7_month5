from django.contrib import admin
from apps.todos.models import Todos, Category
# Register your models here.

@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_completed']
    list_filter = ['id', 'title', 'is_completed']
    search_fields = ['id', 'title', 'is_completed']
    list_editable = ['is_completed', ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
