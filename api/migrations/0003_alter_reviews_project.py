# Generated by Django 5.1.4 on 2024-12-29 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_projects_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.projects'),
        ),
    ]