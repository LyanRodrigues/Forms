from django.db import models
from .choices import PARTICIPANT_DISABILITY_CHOICES
class Disability(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ParticipantResponse(models.Model):
    participant_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender_choices = [
    ('male', 'Masculino'),
    ('female', 'Feminino'),
    ]

    PARTICIPANT_DISABILITY_CHOICES = [
    ('auditiva', 'Deficiência Auditiva'),
    ('fisica', 'Deficiência Física'),
    ('intelectual', 'Deficiência Intelectual'),
    ('visual', 'Deficiência Visual'),
    ('autista', 'Transtorno Espectro Autista'),
    # Add more options as needed
    ]

    gender = models.CharField(max_length=6, choices=gender_choices)
    participant_disability = models.CharField(max_length=255, choices=PARTICIPANT_DISABILITY_CHOICES, default=[''])
    clinical_diagnosis = models.TextField()
    functional_profile = models.TextField()
    participation_modalities = models.TextField()
    participation_observations = models.TextField()
    attendance_frequency = models.IntegerField()
    attended_dates = models.CharField(max_length=255)
    absences_count = models.IntegerField()
    absent_dates = models.CharField(max_length=255, blank=True)
    school_name = models.CharField(max_length=255)
    additional_observations = models.TextField()
    dropout_list = models.TextField(blank=True)
    dropout_reason = models.TextField(blank=True)
    responding_teacher_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Response for {self.participant_name}"
