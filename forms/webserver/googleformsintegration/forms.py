from django import forms
from .models import ParticipantResponse, Disability

class ParticipantResponseForm(forms.ModelForm):
    PARTICIPANT_DISABILITY_CHOICES = [
        ('option1', 'Option 1 Label'),
        ('option2', 'Option 2 Label'),
        # Add more options as needed
    ]

    participant_disability = forms.MultipleChoiceField(
        choices=PARTICIPANT_DISABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='4 - Deficiência do Participante'
    )

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
