# Generated by Django 4.0.1 on 2022-02-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0006_alter_investment_invstmt_ref'),
    ]

    operations = [
        migrations.DeleteModel(
            name='interests_and_bonus',
        ),
    ]
