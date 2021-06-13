# Generated by Django 3.1.2 on 2021-06-10 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('name', models.CharField(default=False, max_length=100)),
                ('skill', models.CharField(default=False, max_length=250)),
            ],
        ),
    ]
