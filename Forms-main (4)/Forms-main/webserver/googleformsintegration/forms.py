from django import forms
from .models import ParticipantResponse

class ParticipantResponseForm(forms.ModelForm):
    class Meta:
        model = ParticipantResponse
        exclude = []  # Add any fields you want to exclude from the form
