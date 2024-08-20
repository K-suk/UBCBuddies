from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import MaleQueue, FemaleQueue

class MaleQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = MaleQueue
        fields = ('id', 'users')

class FemaleQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = FemaleQueue
        fields = ('id', 'users')