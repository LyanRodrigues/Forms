from django.urls import path
from .views import form_view, show_responses

urlpatterns = [
    path('form/', form_view, name='form'),
    path('responses/', show_responses, name='responses'),
]
