from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer

from .serializers import SupersSerializer
from .models import Super
from django.shortcuts import get_object_or_404

# Create your views here.
""""Function view to GET and POST hero or villain"""
@api_view(["GET", "POST"])
def supers_detail(request):
    if request.method == "GET":  
        #query to get super by type
        types = request.query_params.get("super_type") 
        queryset = Super.objects.all()
        if types:
            supers = supers.filter(super_type__type=types)
        serializer = SupersSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
"""Function View to GET, UPDATE, or DELETE using PK"""
@api_view(["GET", "PUT", "DELETE"])
def super_pk_needed (request, pk):
        super = get_object_or_404(Super,pk=pk)
        if request.method == "GET":
            serializer = SupersSerializer(super);
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = SupersSerializer(super,data=request.data);
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        elif request.method == "DELETE":
            super.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
@api_view(["GET"])       
def types_and_supers(request):
    
    supers = Super.objects.all()
    types = SuperType.objects.all()
    
    super_serializer = SupersSerializer(supers, many=True)
    type_serializer = SuperTypeSerializer(types, many=True)
    
    cumston_response_dict = {
        "supers": super_serializer.data,
        "types": type_serializer.data
    }
    return Response(cumston_response_dict)
        


        

        


        

        
    
    

        
        




    
        
    
