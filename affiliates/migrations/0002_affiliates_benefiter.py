# Generated by Django 4.0.1 on 2022-02-02 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affiliates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliates',
            name='benefiter',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
