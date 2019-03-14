# Generated by Django 2.1.7 on 2019-03-06 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(choices=[('PU', 'Puppy'), ('YG', 'Young'), ('AD', 'Adult'), ('SR', 'Senior')], max_length=2)),
                ('size', models.CharField(choices=[('XS', 'Tiny'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2)),
            ],
        ),
    ]
