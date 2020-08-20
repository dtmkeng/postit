from rest_framework import serializers

class GenderSerializer(serializers.Serializer):
    gender = serializers.CharField()

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.DecimalField(max_digits=5, decimal_places=0)
    gender = GenderSerializer()