# Generated by Django 5.0.1 on 2024-02-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0093_alter_users_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)], default=2),
        ),
    ]