# Generated by Django 5.0.1 on 2024-02-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0092_alter_prescription_prescription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=1),
        ),
    ]