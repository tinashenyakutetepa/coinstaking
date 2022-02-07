# Generated by Django 3.2.12 on 2022-02-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0008_alter_investment_amount_in_doge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='total_coins',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
    ]