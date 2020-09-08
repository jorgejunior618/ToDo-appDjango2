from rest_framework import serializers

from .models import Task

## SERIALIZERS NECESSÁRIOS PARA A REQUISIÇÃO DA API AO BANCO DE DADOS,
# E PREPARAR A RESPOSTA PARA RETORNAR EM JSON

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'

