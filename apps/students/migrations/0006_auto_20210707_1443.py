# Generated by Django 3.2.5 on 2021-07-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_alter_student_filiere_bac'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bac_scan',
            field=models.ImageField(blank=True, upload_to='students/BacScan/'),
        ),
        migrations.AddField(
            model_name='student',
            name='releve_notes_scan',
            field=models.ImageField(blank=True, upload_to='students/RelveNotesScan/'),
        ),
    ]
