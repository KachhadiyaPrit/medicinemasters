# Generated by Django 5.0.1 on 2024-02-04 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0079_cart_detail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='education',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
