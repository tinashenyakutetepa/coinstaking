# Generated by Django 4.0.1 on 2022-02-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0005_rename_invstmt_number_investment_invstmt_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='invstmt_ref',
            field=models.CharField(blank=True, max_length=6, unique=True),
        ),
    ]
