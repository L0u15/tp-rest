from django.shortcuts import render
from django.http import Http404

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
        error=[]
        if len(request.data) is 0:
            return Response({"error":"body can't be empty"},status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self,request , pk,format=None):
        todo=self.get_object(pk)
        serializer= TodoSerializer(todo)
        return Response(serializer.data)

    def get_object(self,pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)