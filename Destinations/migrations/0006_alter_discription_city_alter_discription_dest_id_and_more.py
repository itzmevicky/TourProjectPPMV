# Generated by Django 4.0.5 on 2022-06-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Destinations', '0005_discription_delete_discriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discription',
            name='city',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Destinations.cities'),
        ),
        migrations.AlterField(
            model_name='discription',
            name='dest_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Destinations.destinations'),
        ),
        migrations.AlterField(
            model_name='discription',
            name='dest_stat_id',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='Destinations.destinations_states'),
        ),
    ]
