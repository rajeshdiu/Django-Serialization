from rest_framework import serializers

from django import forms


class StudentSerializers(serializers.Serializer):
    id=serializers.IntegerField( )
    Name=serializers.CharField(max_length=100)
    Roll=serializers.IntegerField()
    City=serializers.CharField(max_length=100)
    
    
class StudentForm(forms.Form):
    
    Name=forms.CharField(max_length=100)
    Roll=forms.IntegerField()
    City=forms.CharField(max_length=100)