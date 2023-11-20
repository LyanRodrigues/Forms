from django import forms
from .choices import PARTICIPANT_DISABILITY_CHOICES
from .models import ParticipantResponse, Disability

class ParticipantResponseForm(forms.ModelForm):

    PARTICIPANT_DISABILITY_CHOICES = [(str(disability.id), disability.name) for disability in Disability.objects.all()]
    
    ATTENDANCE_CHOICES = [
        ('', 'Escolha'),
        (0, 'Não frequentou o mês todo'),
        *[(i, str(i)) for i in range(1, 26)],
    ]

    ABSENCES_CHOICES = [
        ('', 'Escolha'),
        *[(str(i), str(i)) for i in range(0, 26)],
    ]

    PARTICIPATION_MODALITIES_CHOICES = [
        ('', 'Escolha'),
        ('Desenvolvimento Motor - Polo artex', 'Desenvolvimento Motor - Polo artex'),
        ('Desenvolvimento Motor - Polo ASMOSABE', 'Desenvolvimento Motor - Polo ASMOSABE'),
        ('Desenvolvimento Motor - Polo Vasto Verde', 'Desenvolvimento Motor - Polo Vasto Verde'),
        ('Equitação Adaptada', 'Equitação Adaptada'),
        ('Ginástica Artística Adaptada - Polo ABLUGO', 'Ginástica Artística Adaptada - Polo ABLUGO'),
        ('Iniciação rendimento Bocha Paralímpica', 'Iniciação rendimento Bocha Paralímpica'),
        ('Iniciação rendimento Goalball', 'Iniciação rendimento Goalball'),
        ('Iniciação rendimento Para-Atletismo', 'Iniciação rendimento Para-Atletismo'),
        ('Iniciação rendimento Para-Natação', 'Iniciação rendimento Para-Natação'),
        ('Iniciação rendimento Tênis de Mesa Paralímpico', 'Iniciação rendimento Tênis de Mesa Paralímpico'),
        ('Para-Natação Escolar - Sede', 'Para-Natação Escolar - Sede'),
        ('EBM Anita Garibaldi', 'EBM Anita Garibaldi'),
        ('EBM Adelaide Starke', 'EBM Adelaide Starke'),
        ('EBM Leoberto Leal', 'EBM Leoberto Leal'),
        ('EBM Visconde de Taunay', 'EBM Visconde de Taunay'),
        ('EBM Felipe Schmidt', 'EBM Felipe Schmidt'),
        ('EBM Lucio Esteves', 'EBM Lucio Esteves'),
        ('EBM João Joaquim Fronza', 'EBM João Joaquim Fronza'),
        ('EBM Wilheim Theodor Schurmann', 'EBM Wilheim Theodor Schurmann'),
        ('EBM Lauro Muller', 'EBM Lauro Muller'),
        ('Iniciação rendimento Futebol PC', 'Iniciação rendimento Futebol PC'),
        ('Iniciação rendimento Futebol DI', 'Iniciação rendimento Futebol DI'),
        # Add more options as needed
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    participant_name = forms.CharField(
        required=True,
        label='1 - Nome do participante'
    )

    birth_date = forms.DateField(
        required=True,
        label='2 - Data de nascimento'
    )

    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        required=True,
        widget=forms.RadioSelect,
        label='3 - Sexo do participante'
    )  

    participant_disability = forms.MultipleChoiceField(
        choices=PARTICIPANT_DISABILITY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='4 - Deficiência do Participante'
    )

    clinical_diagnosis = forms.CharField(
        required=True,
        label='5 - Qual seu diagnóstico clínico?'
    )

    functional_profile = forms.CharField(
        required=True,
        label='6 - Perfil funcional da Deficiência e do participante'
    )

    participation_modalities = forms.ChoiceField(
        choices=PARTICIPATION_MODALITIES_CHOICES,
        required=True,
        label='7 - Participa em qual modalidade?'
    )

    participation_observations = forms.CharField(
        required=False,
        label='8 - Observações da participação do participante neste mês.'
    )

    attendance_frequency = forms.ChoiceField(
        choices=ATTENDANCE_CHOICES,
        required=True,
        label='9 - Quantas vezes o participante frequentou nas aulas neste mês?'
    )

    attended_dates = forms.CharField(
        required=True,
        label='10 - Quais as datas frequentou neste mês: (Exemplo 2,4,6...).'
    )

    absences_count = forms.ChoiceField(
        choices=ABSENCES_CHOICES,
        required=False,
        label='11 - Número de faltas neste mês?'
    )

    absent_dates = forms.CharField(
        required=False,
        label='12 - Quais as datas que não frequentou este mês: (Exemplo 10,12,14...).'
    )

    school_name = forms.CharField(
        required=True,
        label='13 - Nome da Escola que o participante estuda.'
    )

    additional_observations = forms.CharField(
        required=False,
        label='14 - Observações:'
    )

    dropout_list = forms.CharField(
        required=False,
        label='15 - Listar participante desistente:'
    )

    dropout_reason = forms.CharField(
        required=False,
        label='16 - Motivo da desistência:'
    )

    responding_teacher_name = forms.CharField(
        required=True,
        label='17 - Nome do professor que respondeu'
    )

    class Meta:
        model = ParticipantResponse
        exclude = []
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'w3-input', 'id': 'id_birth_date'}),
        }
    def clean_participant_disability(self):
        participant_disability = self.cleaned_data['participant_disability']
        if not participant_disability:
            raise forms.ValidationError("Select at least one disability.")
        return participant_disability
    def __init__(self, *args, **kwargs):
        super(ParticipantResponseForm, self).__init__(*args, **kwargs)
        self.fields['participant_disability'].choices = PARTICIPANT_DISABILITY_CHOICES