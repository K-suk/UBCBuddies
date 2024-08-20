from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'first_name', 
            'last_name', 
            'age', 
            'sex', 
            'contact_address', 
            'cur_matching', 
            'matching_history', 
            'bio', 
            'wait', 
            'done', 
            'is_active', 
            'is_staff', 
            'created_at', 
            'updated_at'
        )
        read_only_fields = ('is_active', 'is_staff', 'created_at', 'updated_at')