from rest_framework.decorators import api_view
from rest_framework.response import Response

from supers.serializer import SuperSerializer
from .serializer import SuperTypeClass
from .models import Super_type

# Create your views here.

@api_view(['Get'])

def super_types_list(request):

    super_types = Super_type.objects.all()

    serializer = SuperSerializer(super_types, many=True)


    return Response(serializer.data)