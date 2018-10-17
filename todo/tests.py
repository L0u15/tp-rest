from django.test import TestCase

# Create your tests here.
from todo.models import Todo
todo1 = Todo(description="faire courses",priority="high")
todo1.save()
todo2=Todo(description="aller à la plage")
todo2.save()

todos = Todo.objects.all()
for todo in todos:
    print("%d %s"%(todo.id,todo.description))

todos = Todo.objects.filter(priority="low")

from todo.serializers import TodoSerializer
serializer = TodoSerializer(todo1)
print('%s'%(serializer.data))

from rest_framework.renderers import JSONRenderer
content = JSONRenderer().render(serializer.data)
print(content)

# from todo import tests