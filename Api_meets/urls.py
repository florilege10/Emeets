from django.urls import path
from .views import (
    PublicationListForMenView, LikeCreateView, AbonnementCreateView, MessageCreateView,
    PublicationListForWomenView, LikeListForWomenView, MessageListForWomenView,
    PhotoListCreateView, PhotoRetrieveUpdateDestroyView, UserDetailView, UserListView, UserUpdateView, home
)

urlpatterns = [
    path('', home, name='home'),
    path('men/publications/', PublicationListForMenView.as_view(), name='men_publications'),
    path('men/like/', LikeCreateView.as_view(), name='men_like'),
    path('men/abonnement/', AbonnementCreateView.as_view(), name='men_abonnement'),
    path('men/message/', MessageCreateView.as_view(), name='men_message'),
    path('women/publications/', PublicationListForWomenView.as_view(), name='women_publications'),
    path('women/likes/', LikeListForWomenView.as_view(), name='women_likes'),
    path('women/messages/', MessageListForWomenView.as_view(), name='women_messages'),
    path('photos/', PhotoListCreateView.as_view(), name='photo_list_create'),
    path('photos/<int:pk>/', PhotoRetrieveUpdateDestroyView.as_view(), name='photo_retrieve_update_destroy'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),

]