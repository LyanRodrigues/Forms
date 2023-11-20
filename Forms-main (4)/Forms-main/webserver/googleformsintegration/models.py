from django.db import models

class ParticipantResponse(models.Model):
    participant_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    gender_choices = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    disability_choices = [
        ('DA', 'Deficiência Auditiva'),
        ('DF', 'Deficiência Física'),
        ('DI', 'Deficiência Intelectual'),
        ('DV', 'Deficiência Visual'),
        ('TEA', 'Transtorno Espectro Autista'),
    ]
    participant_disability = models.CharField(max_length=3, choices=disability_choices)
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
