# Generated by Django 4.0.5 on 2022-06-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destinations_states',
            name='id',
        ),
        migrations.AddField(
            model_name='destinations_states',
            name='states_Id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
