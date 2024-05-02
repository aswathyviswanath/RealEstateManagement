
from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    first_name = serializers.CharField(max_length=50) 
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)



    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password', 'password2','user_type')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self,validated_data):
        
        username = validated_data['username']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        password = validated_data['password']
        user_type=validated_data['user_type']
        reg_user = User(email=email, username=username,first_name=first_name,last_name=last_name,user_type=user_type)
        reg_user.set_password(password)
        reg_user.save()

        return reg_user
    

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


