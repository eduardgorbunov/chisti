# Generated by Django 2.0.4 on 2018-05-12 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20180421_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='add_from_administration',
            field=models.BooleanField(db_index=True, default=True, verbose_name='Из админки'),
        ),
    ]