# Generated by Django 3.1.7 on 2021-04-18 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210417_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattendees',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]
