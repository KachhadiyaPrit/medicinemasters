# Generated by Django 5.0.1 on 2024-02-04 07:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0078_alter_users_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_detail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
