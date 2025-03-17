from rest_framework import serializers
from .models import User, Publication, Like, Abonnement, Message, Photo
from dj_rest_auth.registration.serializers import RegisterSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'sexe', 'address', 'role']

class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Publication
        fields = ['id', 'user', 'image', 'timestamp']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'publication', 'timestamp']

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = ['id', 'user', 'start_date', 'duration_days', 'tarif', 'expires_at', 'is_active']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'image', 'timestamp', 'is_read', 'parent_message']

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'user', 'image', 'uploaded_at']



from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.core.exceptions import ValidationError
class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=15, required=False, allow_blank=True)
    sexe = serializers.ChoiceField(choices=[("H", "Homme"), ("F", "Femme")], required=True)
    address = serializers.CharField(max_length=255, required=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data.update({
            'phone_number': self.validated_data.get('phone_number', ''),
            'sexe': self.validated_data.get('sexe'),
            'address': self.validated_data.get('address'),
        })
        return data

    def save(self, request):
        user = super().save(request)
        user.phone_number = self.validated_data.get('phone_number', '')
        user.sexe = self.validated_data.get('sexe')
        user.address = self.validated_data.get('address')
        user.is_active = True
        user.save()
        return user