# Generated by Django 5.0.1 on 2024-01-18 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0046_offer_offer_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1),
        ),
    ]
