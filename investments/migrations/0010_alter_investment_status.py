# Generated by Django 3.2.12 on 2022-02-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0009_alter_bank_total_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
