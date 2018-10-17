from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import status

from todo.models import Todo
from todo.serializers import TodoSerializer


# Create your views here.
class TodoList(APIView):
    """
    List all snippets, or create a new snippet
    """
    def get(self,request, format=None):
        todos=Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print(request.data)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response