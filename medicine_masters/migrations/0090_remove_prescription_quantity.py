# Generated by Django 5.0.1 on 2024-02-17 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0089_prescription_order_detail_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='quantity',
        ),
    ]