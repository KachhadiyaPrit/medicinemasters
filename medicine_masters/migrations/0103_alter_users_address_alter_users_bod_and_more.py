# Generated by Django 5.0.1 on 2024-03-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine_masters', '0102_rename_pyment_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='bod',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='pincode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]