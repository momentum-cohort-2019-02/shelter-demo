# Generated by Django 2.1.7 on 2019-03-11 20:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_add_dogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
