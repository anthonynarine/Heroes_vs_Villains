from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType

from .serializers import SupersSerializer
from .models import Super
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(["GET", "POST"])
def supers_detail(request):
    if request.method == "GET":  
        queryset = Super.objects.all()
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
def super_detail (request, pk):
    try:
        super = Super.objects.get(pk=pk)
        serializer = SupersSerializer(super);
        return Response(serializer.data)
    except Super.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

        
    
    
    
    print(pk)
    return Response(pk)
    


        
        




    
        
    
