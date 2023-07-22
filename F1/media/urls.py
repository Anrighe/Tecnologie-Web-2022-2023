from django.urls import path
from .models import *
from . import views

from media.views import HomePageView, HighlightPageView, VideoHighlightPageView

app_name = 'media'

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('highlight/', HighlightPageView.as_view(), name='highlight'),
    path('highlight/<pk>/', VideoHighlightPageView.as_view(), name='highlight_video'),
]
