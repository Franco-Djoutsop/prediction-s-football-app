from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import check_password 


from .models import Bettor

#|__________________________________________________________________________________________|
#|  c'est ici qu'on converti les informations enregistrees dans la db en format js    |
#|__________________________________________________________________________________________|


#Serializer to Get User Details using Django Token Authentication
class BettorSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Bettor
        fields = ('id', 'number', 'email','password')
        
        
#|_________________________________|
#|  creation du nouvel utilisateur |
#|_________________________________|



#Serializer to Register User
class SignupSerializer(serializers.ModelSerializer):
    email =  serializers.EmailField(required = True,
                                    validators = [UniqueValidator(queryset = Bettor.objects.all())]
                                    )
    
    password = serializers.CharField(write_only = True,
                                     required = True,
                                     validators = [validate_password])
    
    class Meta: 
        model = Bettor
        fields = ('id', 'number', 'email','password')
        
    
    def create(self, validated_data):
        user = Bettor.objects.create(
            email = validated_data['email'],
            number = validated_data['number']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    

#|_________________________________|
#|  creation champs pour se loguer |
#|_________________________________|


class LoginEmailSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='your email', write_only=True)
    password = serializers.CharField(label= "your password", style ={'input_type' : 'password'}, write_only = True)
    
    class Meta:
        model = Bettor
        fields = ('id','email','password')
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        
        if email and password : 
            user = authenticate(request = self.context.get('request'),
                                email=email,
                                password=password)

            if not user:
                msg = "access denied : wrong email or password ."
                raise serializers.ValidationError(msg, code = 'authorization')

        else:
            msg= 'Both "email" and "password" are required.'
            raise serializers.ValidationError(msg, code = 'authorization')
        attrs['user'] = user
    
        return attrs
    

class LoginNumberSerializer(serializers.ModelSerializer):
    number = serializers.CharField(label='your number', write_only=True)
    password = serializers.CharField(label= "your password", style ={'input_type' : 'password'}, write_only = True)

    class Meta:
        model = Bettor
        fields = ('id','number','password')

    def validate(self, attrs):
        number = attrs.get('number')
        password = attrs.get('password')

        if number and password : 
            user = authenticate(request = self.context.get('request'),
                                number=number,
                                password=password)

            if not user:
                msg = "access denied : wrong number or password ."
                raise serializers.ValidationError(msg, code = 'authorization')

        else:
            msg= 'Both "email" and "password" are required . '
            raise serializers.ValidationError(msg, code = 'authorization')
        attrs['user'] = user

        return attrs

class MyNumberBackend(object):
    def authenticate(self, username = None, password = None):
        my_user_model = get_user_model()
        try:
            user = my_user_model.objects.get(number = username)
            if user.check_password(password):
                return user
        except my_user_model.DoesNotExist:
            return None
        except:
            return None

    def get_user(self, user_id):
        my_user_model = get_user_model()
        try:
            return my_user_model.objects.get(pk = user_id)
        except my_user_model.DoesNotExist:
            return None
        