from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import FemaleDatingQueue, FemaleDrinkQueue, FemaleGymQueue, MaleDatingQueue, MaleDrinkQueue, MaleGymQueue, MaleQueue, FemaleQueue

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
        
class MaleGymQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = MaleGymQueue
        fields = ('id', 'users')

class FemaleGymQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = FemaleGymQueue
        fields = ('id', 'users')
        
class MaleDrinkQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = MaleDrinkQueue
        fields = ('id', 'users')

class FemaleDrinkQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = FemaleDrinkQueue
        fields = ('id', 'users')
        
class MaleDatingQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = MaleDatingQueue
        fields = ('id', 'users')

class FemaleDatingQueueSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = FemaleDatingQueue
        fields = ('id', 'users')