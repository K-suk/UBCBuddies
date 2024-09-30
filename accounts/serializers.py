from rest_framework import serializers
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

User = get_user_model()

SEX_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class UserSerializer(serializers.ModelSerializer):
    sex = serializers.ChoiceField(choices=SEX_CHOICES)
    
    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'name',
            'age', 
            'sex', 
            'contact_address', 
            'cur_matching', 
            'matching_history', 
            'bio',
            'profile_image',
            'wait', 
            'done', 
            'is_active', 
            'is_staff', 
            'is_superuser',
            'created_at', 
            'updated_at',
            'review_count',
            'review_sum',
            'semi_comp',
        )
        read_only_fields = ('is_active', 'is_staff', 'created_at', 'updated_at')
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'contact_address', 'bio', 'age', 'profile_image')
        
class UserCreateSerializer(BaseUserCreateSerializer):
    def validate(self, attrs):
        # バリデーションの開始をログに出力
        print("Validation started with data:", attrs)
        
        if attrs['password'] != attrs['re_password']:
            # パスワードが一致しない場合のエラーをログに出力
            print("Validation error: Passwords do not match")
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        # バリデーションが成功した場合のデータをログに出力
        print("Validation successful:", attrs)
        return attrs

    def create(self, validated_data):
        # ユーザー作成の開始をログに出力
        print("User creation started with validated data:", validated_data)
        
        try:
            user = User.objects.create_user(
                email=validated_data['email'],
                name=validated_data.get('name'),
                password=validated_data['password']
            )
            # ユーザー作成の成功をログに出力
            print("User created successfully:", user)
        except Exception as e:
            # エラーが発生した場合、エラーをログに出力
            print(f"Error creating user: {e}")
            raise
        return user

    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 
            'email', 
            'name', 
            'age', 
            'sex', 
            'contact_address', 
            'password',
            're_password',  # パスワード確認用フィールド
            'cur_matching', 
            'matching_history', 
            'bio',
            'profile_image',
            'wait', 
            'done', 
            'is_active', 
            'is_staff', 
            'created_at', 
            'updated_at',
            'review_count',
            'review_sum',
            'semi_comp',
        )
        read_only_fields = ('is_active', 'is_staff', 'created_at', 'updated_at')