# Generated by Django 3.2.12 on 2022-02-03 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interests', '0004_auto_20220203_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest_Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_interest_coins', models.DecimalField(blank=True, decimal_places=2, default=65, max_digits=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]