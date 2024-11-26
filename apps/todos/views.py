from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from apps.todos.models import Todos
from apps.todos.serializers import TodosSerializer
from apps.todos.permissions import IsAdminOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# ViewSet для управления задачами
class TodosViewSets(viewsets.ModelViewSet):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [IsAdminOrReadOnly]

# Класс для удаления всех задач
class DeleteAllTodosView(APIView):
    permission_classes = [IsAdminUser]  # Убедитесь, что только администраторы могут удалять все задачи

    def delete(self, request):
        # Удаляем все задачи
        Todos.objects.all().delete()
        return Response({"message": "All todos deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
