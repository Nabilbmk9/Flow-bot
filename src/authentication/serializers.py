from rest_framework import serializers
from .models import CustomUser


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')