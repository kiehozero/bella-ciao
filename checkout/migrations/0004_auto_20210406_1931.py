# Generated by Django 3.1.7 on 2021-04-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20210404_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]