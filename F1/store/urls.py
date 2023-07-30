from django.urls import path
from store.views import UserProfile, UserProfileDataChangeViewUpdate, StoreView

app_name = 'store'

urlpatterns = [
    path('profile/', UserProfile, name='profile'),
    path('profile/modify/<int:pk>/', UserProfileDataChangeViewUpdate.as_view(), name='modify_update'),
    path('store/', StoreView.as_view(), name='store'),
]
