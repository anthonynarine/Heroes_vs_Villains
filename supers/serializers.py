from rest_framework import serializers
from .models import Super


class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields =  ["id","name", "alter_ego", "primary_ability", 
                   "secondary_ability","catchphrase", "super_type", "super_type_id"
                   ]
        depth = 1
    super_type_id = serializers.IntegerField(write_only=True)
   
""" adding super_type_id to our fields list will provide the ability 
    to send super_type id in the body a POST request.

   once the id value is added to the fields list we must override it's 
   default value to write_only.  This is because we do not want this 
   new super_type_id to show up in the serialized response, but we do 
   want to the seriaizer to accept such a value on incoming POST request
   bodies. NOTE the block indent.   """
   
   
   
   
   


