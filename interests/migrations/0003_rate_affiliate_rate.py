# Generated by Django 4.0.1 on 2022-02-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interests', '0002_alter_rate_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='affiliate_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=10, max_digits=15),
            preserve_default=False,
        ),
    ]
