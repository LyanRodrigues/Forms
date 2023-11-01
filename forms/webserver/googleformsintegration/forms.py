from django import forms
from .models import ParticipantResponse
from .models import Disability

class ParticipantResponseForm(forms.ModelForm):
    class Meta:
        model = ParticipantResponse
        exclude = []  
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'w3-input', 'id': 'id_birth_date'}),
            'participant_disability': forms.CheckboxSelectMultiple,
            # Add more widget customizations for other fields if needed
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant_disability'].queryset = Disability.objects.all()