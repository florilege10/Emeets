from rest_framework import generics, permissions
from .models import Publication, Like, Abonnement, Message, Photo
from .serializers import PublicationSerializer, LikeSerializer, AbonnementSerializer, MessageSerializer, PhotoSerializer
from .permissions import IsMan, IsWoman
from Api_meets import serializers
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

# Routes pour les hommes
class PublicationListForMenView(generics.ListAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsMan]

    def get_queryset(self):
        return Publication.objects.filter(user__sexe='F')

class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsMan]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AbonnementCreateView(generics.CreateAPIView):
    serializer_class = AbonnementSerializer
    permission_classes = [permissions.IsAuthenticated, IsMan]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsMan]

    def perform_create(self, serializer):
        if not self.request.user.abonnement_set.filter(is_active=True).exists():
            raise serializers.ValidationError("Vous devez avoir un abonnement actif pour envoyer un message.")
        serializer.save(sender=self.request.user)

# Routes pour les femmes
class PublicationListForWomenView(generics.ListCreateAPIView):
    serializer_class = PublicationSerializer
    permission_classes = [permissions.IsAuthenticated, IsWoman]

    def get_queryset(self):
        return Publication.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeListForWomenView(generics.ListAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated, IsWoman]

    def get_queryset(self):
        return Like.objects.filter(publication__user=self.request.user)

class MessageListForWomenView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsWoman]

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user)

# Routes pour les photos
class PhotoListCreateView(generics.ListCreateAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PhotoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Photo.objects.filter(user=self.request.user)
    
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer


from django.shortcuts import render
from django.views import View

class RegistrationFormView(View):
    def get(self, request):
        return render(request, 'registration/registration.html')