# Generated by Django 3.2.12 on 2022-02-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0005_interest_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest_bank',
            name='total_interest_coins',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
    ]
