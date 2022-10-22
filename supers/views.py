from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SupersSerializer
from .models import Super

# Create your views here.
@api_view(["GET"])
def supers_detail(request):
    queryset = Super.objects.all()
    serializer = SupersSerializer(queryset, many=True)
    return Response(serializer.data)
    
        
    
