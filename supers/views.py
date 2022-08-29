from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from .models import Super

# Create your views here.

@api_view(['GET', 'POST'])

def supers_list(request):
    
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)
   
   
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)