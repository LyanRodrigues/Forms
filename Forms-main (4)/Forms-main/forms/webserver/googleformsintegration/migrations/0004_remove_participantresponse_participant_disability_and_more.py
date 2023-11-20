# Generated by Django 4.2.6 on 2023-11-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleformsintegration', '0003_alter_participantresponse_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participantresponse',
            name='participant_disability',
        ),
        migrations.AddField(
            model_name='participantresponse',
            name='participant_disability',
            field=models.ManyToManyField(to='googleformsintegration.disability'),
        ),
    ]
