from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a  name filed for testing out APIView """
    name= serializers.CharField(max_length=100)

class SquareSerializer(serializers.Serializer):
    x=serializers.IntegerField()
    y=serializers.IntegerField()
    
