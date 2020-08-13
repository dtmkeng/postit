from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.DecimalField(max_digits=5, decimal_places=0)