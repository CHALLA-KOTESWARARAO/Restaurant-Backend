from rest_framework import serializers
from .models import OrdersTB
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrdersTB
        fields='__all__'
    

