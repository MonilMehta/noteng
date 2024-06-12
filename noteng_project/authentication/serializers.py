from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['sapid', 'password', 'email', 'fname', 'lname', 'contact_number']  

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
class TokenObtainPairSerializer(serializers.Serializer):
    default_error_messages = {
        'no_active_account': 'No active account found with the given credentials'
    }
    id = serializers.CharField(source='sapid', read_only=True)
    sapid = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        sapid = attrs.get('sapid')
        password = attrs.get('password')

        if sapid and password:
            user = User.objects.filter(sapid__iexact=sapid).first()  
            if user and user.check_password(password):
                if not user.is_active:
                    raise serializers.ValidationError(self.default_error_messages['no_active_account'])
                refresh = RefreshToken.for_user(user)
                return {
                    'id': user.sapid,
                    'sapid': user.sapid,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
        raise serializers.ValidationError('Unable to login with provided credentials.')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['sapid', 'fname', 'lname', 'email', 'contact_number', 'mentors', 'expertise']

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)