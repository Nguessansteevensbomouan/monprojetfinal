# Generated by Django 5.1.2 on 2024-12-15 03:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_debut', models.DateField()),
                ('date_fin', models.DateField(blank=True, null=True)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cv_projets', to='cv.cv')),
            ],
        ),
    ]
