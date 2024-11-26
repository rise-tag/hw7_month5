from rest_framework import serializers

from apps.todos.models import Todos

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'