from rest_framework.decorators import api_view
## CONSTANTE STATUS CONTEM AS RESPOSTAS HTTP DEVIDAS PARA RETORNO DOS DADOS
from rest_framework import generics, status
from django.core.exceptions import ObjectDoesNotExist
## FUNÇÃO QUE RETORNA OS DADOS EM JSON
from django.http import JsonResponse
import json

from .models import Task
from .serializers import TaskSerializer

## CHAVE ```@api_view(["METHOD"])``` PARA DEFINIR A REQUISIÇÃO
# QUE SERÁ FEITA AO BANCO DE DADOS
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    JSONObj = JsonResponse({'tasks': serializer.data}, safe=False, status=status.HTTP_200_OK)
    return JSONObj

@api_view(['POST'])
def newTask(request):
    form = json.loads(request.body)

    print('Formulario: ', form)

    try:
        task = Task.objects.create(
            title=form['title'],
            description=form['description']
        )

        serializer = TaskSerializer(task)
        return JsonResponse(
            {'task': serializer.data},
            safe=False,
            status=status.HTTP_201_CREATED
        )
    
    except ObjectDoesNotExist as error:
        return JsonResponse(
            {'error': str(error)},
            safe=False,
            status=status.HTTP_404_NOT_FOUND
        )
    
    except Exception:
        return JsonResponse(
            {'error': 'Something went wrong'},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['DELETE'])
def deleteTask(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse(
            {'success': 'Task successfuly deleted'},
            status=status.HTTP_204_NO_CONTENT
        )
    
    except ObjectDoesNotExist as error:
        return JsonResponse(
            { 'error': str(error) },
            safe=False,
            status=status.HTTP_404_NOT_FOUND
        )

    except Exception:
        return JsonResponse(
            {'error': 'Something went wrong'},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# FALTOU TESTE
@api_view(['PUT'])
def editTask(request, taskId):
    form = json.loads(request.body)

    try:
        taskToUpdate = Task.objects.filter(id=taskId)
        taskToUpdate.update(**form)

        task = Task.objects.get(id=taskId)
        serializer = TaskSerializer(task)
        return JsonResponse(
            {'task': serializer.data},
            safe=False,
            status=status.HTTP_200_OK
        )
    
    except ObjectDoesNotExist as error:
        return JsonResponse(
            {'error': str(error)},
            safe=False,
            status=status.HTTP_404_NOT_FOUND
        )
    
    except Exception:
        return JsonResponse(
            {'error': 'Something went wrong'},
            safe=False,
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
