from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from PIL import Image

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    sexe = models.CharField(max_length=1, choices=[("H", "Homme"), ("F", "Femme")])
    address = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=10, choices=[("user", "Utilisateur"), ("admin", "Administrateur")], default="user")

    def __str__(self):
        return self.username

class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'sexe': 'F'})
    image = models.ImageField(upload_to='publications/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 600 or img.width > 600:
                img.thumbnail((600, 600))
                img.save(self.image.path)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'sexe': 'H'})
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} a liké {self.publication.id}"

class Abonnement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'sexe': 'H'})
    start_date = models.DateTimeField(auto_now_add=True)
    duration_days = models.IntegerField()
    tarif = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def expires_at(self):
        return self.start_date + timedelta(days=self.duration_days)

    def is_active(self):
        return timezone.now() < self.expires_at

    def __str__(self):
        return f"Abonnement {self.user.username} - Expire le {self.expires_at}"

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='messages/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"Message de {self.sender.username} à {self.receiver.username}"

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo de {self.user.username}"