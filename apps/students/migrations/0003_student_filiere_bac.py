# Generated by Django 3.2.5 on 2021-07-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='filiere_bac',
            field=models.CharField(choices=[('sciencesMaths', 'sciencesMaths'), ('sciencesPhysique', 'sciencesMaths'), ('svt', 'svt')], default='sciences maths', max_length=20),
        ),
    ]
