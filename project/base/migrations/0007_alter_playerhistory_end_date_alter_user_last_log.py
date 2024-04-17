# Generated by Django 5.0.4 on 2024-04-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_playerhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerhistory',
            name='end_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_log',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
