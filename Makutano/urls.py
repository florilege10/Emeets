from django.contrib import admin
from django.urls import path, include

from Api_meets.views import CustomRegisterView, RegistrationFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/', include('Api_meets.urls')),  # Assurez-vous que cette ligne est correcte
    #path('auth/registration/', CustomRegisterView.as_view(), name='custom_register'),
    path('auth/registration/form/', RegistrationFormView.as_view(), name='registration_form'),
]