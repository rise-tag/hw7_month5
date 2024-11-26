from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.todos.views import TodosViewSets

router = DefaultRouter()
router.register("api_todos", TodosViewSets, basename='api-todos')
router.register("todos_viewsets", TodosViewSets, basename='api-todos-viewsets')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
