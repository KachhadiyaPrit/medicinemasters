# Generated by Django 5.0 on 2024-01-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0052_alter_offer_offer_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer_rate',
            field=models.IntegerField(null=True),
        ),
    ]
