from django.urls import path
from .views import HumanCreateView


urlpatterns = [
    path('create/', HumanCreateView.as_view()),
]
