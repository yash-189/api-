from rest_framework import serializers
from .models import months,user



class MonthSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = months
        fields = ('__all__')
        



class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = user
        fields = ('__all__')

